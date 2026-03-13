from serpapi import GoogleSearch
from config.config import SERPAPI_API_KEY


def search_web(query):

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    snippets = []

    if "organic_results" in results:
        for result in results["organic_results"][:3]:
            snippets.append(result.get("snippet", ""))

    return "\n".join(snippets)
