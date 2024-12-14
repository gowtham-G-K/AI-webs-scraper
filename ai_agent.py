import time
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the prompt template that will be used to extract the relevant information
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the Ollama model
model = OllamaLLM(model="llama3.1")

# Function to parse and extract relevant details from the DOM chunks
def parse_with_ollama(dom_chunks):
    # Create a ChatPromptTemplate with the defined template
    prompt = ChatPromptTemplate.from_template(template)
    # Create a chain by connecting the prompt to the model
    chain = prompt | model
    results = {}
    
    # Define a list of questions to be asked for each DOM chunk
    questions = [
        "Based on the provided content, which industry does it belong to?",
        "Based on the provided content, is the size of the industry small, medium, or large?",
        "Based on the provided content, what is the geographic location or region where this industry is primarily based?"
    ]

    # Iterate through each question and process each DOM chunk with the model
    for question in questions:
        parsed_results = []
        for i, chunk in enumerate(dom_chunks, start=1):
            # Invoke the chain with the current DOM chunk and question
            response = chain.invoke(
                {"dom_content": chunk, "parse_description": question}
            )
            print(f"Parsed batch: {i} of {len(dom_chunks)}")
            parsed_results.append(response)
        
        # Join all responses for the current question and store them
        results[question] = "\n".join(parsed_results)
        
        # Adding a sleep time to avoid overloading the model with requests
        time.sleep(5)

    # Return the results in a structured format
    return {
        "industry": results.get(questions[0], "Unknown"),
        "company_size": results.get(questions[1], "Unknown"),
        "location": results.get(questions[2], "Unknown"),
    }
