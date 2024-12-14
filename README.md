# FastAPI Scraper and AI Parser

This project is a FastAPI-based web application that:
1. Scrapes web pages to extract content.
2. Parses the content using an AI model to extract specific details like industry, company size, and location.

The application uses `BeautifulSoup` for web scraping and an AI model integration via LangChain for parsing.

## Features
- Web scraping functionality to fetch and clean web page content.
- AI-powered parsing to extract structured information.
- Secure authentication using a secret key via the `Authorization` header.

---

## Requirements

### Prerequisites
- Python 3.8+
- `pip` (Python package installer)

### Dependencies
Install required dependencies using:
```bash
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file or set the following environment variables:
```plaintext
SECRET_KEY=your-secret-key
```
This key is used to authenticate requests.

---

## Project Structure
```
project-directory/
├── main.py          # FastAPI entry point
├── ai_agent.py      # AI parsing logic
├── scraper.py       # Web scraping functions
├── models.py        # Pydantic models for request/response
├── config.py        # Configuration file for environment variables
├── requirements.txt # Python dependencies
└── Procfile         # Process declaration for deployment
```

---

## Usage

### Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo.git
   cd your-repo
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   export SECRET_KEY=your-secret-key
   ```

4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

5. Access the API at: `http://127.0.0.1:8000`

### Endpoints
#### 1. `/scrape-and-answer`
- **Method**: POST
- **Description**: Scrapes a web page and extracts relevant information.
- **Request Body**:
  ```json
  {
      "url": "https://example.com"
  }
  ```
- **Headers**:
  ```plaintext
  Authorization: Bearer your-secret-key
  ```
- **Response**:
  ```json
  {
      "industry": "Technology",
      "company_size": "Medium",
      "location": "USA"
  }
  ```

---

## Testing
- Use tools like [Postman](https://www.postman.com/) or `curl` to test the API.
- Example `curl` command:
  ```bash
  curl -X POST \
       -H "Authorization: Bearer your-secret-key" \
       -H "Content-Type: application/json" \
       -d '{"url": "https://example.com"}' \
       http://127.0.0.1:8000/scrape-and-answer
  ```

---

## Future Improvements
- Enhance error handling for edge cases in scraping and parsing.
- Add support for more AI models.
- Extend the functionality to handle dynamic web pages.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

