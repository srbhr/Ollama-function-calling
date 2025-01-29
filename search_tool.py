import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

def web_search(query: str) -> Dict[Any, Any]:
    load_dotenv()
    api_key = os.getenv('SEARCH_API_KEY')
    
    if not api_key:
        return {"error": "API key not found in environment variables"}
    
    url = "https://www.searchapi.io/api/v1/search"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    params = {
        "engine": "google_news",
        "q": query,
        "num": 5
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 401:
            return {"error": "Invalid API key or authentication failed"}
        elif response.status_code == 429:
            return {"error": "Rate limit exceeded"}
        
        response.raise_for_status()
        return response.json()
        
    except requests.exceptions.RequestException as e:
        error_msg = f"Error fetching search results: {e}"
        if hasattr(e, 'response') and e.response:
            try:
                error_details = e.response.json()
                error_msg = f"{error_msg} - {error_details.get('message', '')}"
            except:
                pass
        return {"error": error_msg}

def extract_content(search_results: dict) -> str:
    content = []
    
    if "organic_results" in search_results:
        for result in search_results["organic_results"][:4]:  # Top 4 results
            if "snippet" in result:
                content.append(result["snippet"])
                
    if "answer_box" in search_results and search_results["answer_box"]:
        if "answer" in search_results["answer_box"]:
            content.insert(0, search_results["answer_box"]["answer"])
            
    return "\n\n".join(content)