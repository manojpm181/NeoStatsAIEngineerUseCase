from langchain_community.utilities import SerpAPIWrapper
from config.config import SERP_API_KEY


def search_web(query):

    try:

        search = SerpAPIWrapper(
            serpapi_api_key=SERP_API_KEY
        )

        result = search.run(query)

        return result

    except Exception as e:

        return f"Web search error: {str(e)}"