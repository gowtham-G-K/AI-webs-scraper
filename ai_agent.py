from transformers import pipeline

def get_company_details(dom_chunks):
    # Initialize the pipelines
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # Summarization model
    qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")  # Question-answering model

    # Combine all the chunks into one large text
    full_text = " ".join(dom_chunks)

    # Summarize the full text into a concise version
    summary = summarizer(full_text, max_length=500, min_length=150, do_sample=False)[0]['summary_text']

    # Define the questions
    questions = [
        "Based on the provided content, what industry is being discussed?",
        "Based on the provided content, what is the size of the company or industry?",
        "Based on the provided content, what geographic location or region is mentioned?"
    ]

    # Prepare a dictionary for storing the answers
    results = {}

    # Process each question
    for question in questions:
        answer = qa_pipeline({
            'question': question,
            'context': summary  # Use the summarized content for Q&A
        })
        results[question] = answer['answer']

    # Return structured results
    return {
        "industry": results.get(questions[0], "Unknown"),
        "company_size": results.get(questions[1], "Unknown"),
        "location": results.get(questions[2], "Unknown"),
    }

