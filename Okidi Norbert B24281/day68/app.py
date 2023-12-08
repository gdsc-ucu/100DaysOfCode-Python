import requests

class APIError(Exception):
    def __init__(self, message):
        super().__init__(message)

def get_news_headlines(category):
    api_key = "4da3790013d1488aa293dab74429ea81"
    endpoint = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={api_key}"
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as err:
        raise APIError(f"HTTP Error: {err}")
    except Exception as e:
        raise APIError(f"An unexpected error occurred: {e}")
    
try:
    user_category = input("Enter a news category (e.g., business, technology, health): ")
    news_data = get_news_headlines(user_category.lower())
    

    if "articles" in news_data:
        articles = news_data["articles"]
        print(f"\nTop Headlines in the {user_category.capitalize()} category:\n")

        for index, article in enumerate(articles, start=1):
            title = article.get("title", "No Title")
            description = article.get("description", "No Description")
            url = article.get("url", "#")

            print(f"{index}. {title}")
            print(f"   Description: {description}")
            print(f"   URL: {url}\n")
    else:
        print(f"No articles found for the specified category.")

except APIError as api_error:
    print(f"API Error: {api_error}")