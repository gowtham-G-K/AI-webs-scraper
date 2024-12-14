import requests
from bs4 import BeautifulSoup


def fetch_static_content(url: str) -> str:
    """
    Fetch static content from the given URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error fetching static content: {e}")


def extract_body_content(html_content: str) -> str:
    """
    Extract the body content from the HTML.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content: str) -> str:
    """
    Clean the body content by removing script and style tags
    and extracting the text.
    """
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get cleaned text
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content


def split_dom_content(dom_content: str, max_length: int = 6000) -> list:
    """
    Split the DOM content into chunks of a specified maximum length.
    """
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]


def get_web_page_content(url: str) -> list:
    """
    Fetch and process the web page content from the specified URL.
    """
    page_content = fetch_static_content(url)
    body_content = extract_body_content(page_content)
    clean_content = clean_body_content(body_content)
    return split_dom_content(clean_content)
