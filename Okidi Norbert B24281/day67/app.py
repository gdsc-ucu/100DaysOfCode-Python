import requests

def get_news_headlines(category):
    api_key = "4da3790013d1488aa293dab74429ea81"
    endpoint = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={api_key}"
    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])

        print(f"\nTop Headlines in the {category.capitalize()} category:\n")

        for index, article in enumerate(articles, start=1):
            title = article.get("title", "No Title")
            description = article.get("description", "No Description")
            url = article.get("url", "#")

            print(f"{index}. {title}")
            print(f"   Description: {description}")
            print(f"   URL: {url}\n")
    else:
        print(f"Error: Unable to fetch news headlines for the {category} category.")

user_category = input("Enter a news category (e.g., business, technology, health): ")
get_news_headlines(user_category.lower())
