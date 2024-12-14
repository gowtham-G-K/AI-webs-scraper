from config import SECRET_KEY
from ai_agent import parse_with_ollama
from scraper import get_web_page_content
from models import URLInput, ScrapingResponse
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/scrape-and-answer", response_model=ScrapingResponse)
async def scrape_and_answer(url: URLInput, authorization: str = Header(None)):

    # Check for Authorization header
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization header missing")
    
    # Validate Authorization header
    if authorization != f"Bearer {SECRET_KEY}":
        raise HTTPException(status_code=401, detail="Invalid Authorization header")

    try:
        # Asynchronously get the content of the web page
        content = await get_web_page_content(url.url)

        # Parse the content with the AI agent function
        parsed_result = await parse_with_ollama(content)

        # Return the parsed result
        return parsed_result

    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
