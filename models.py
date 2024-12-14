from pydantic import BaseModel, HttpUrl
from typing import Optional

class URLInput(BaseModel):
    url: HttpUrl

class ScrapingResponse(BaseModel):
    industry: Optional[str] = None  # Optional field, defaults to None if missing
    company_size: Optional[str] = None  # Optional field, defaults to None if missing
    location: Optional[str] = None  # Optional field, defaults to None if missing
