import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('div', class_='article')
        return data
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return []


def scrape_multiple_pages(base_url, num_pages):
    all_data = []
    for page_num in range(1, num_pages + 1):
        page_url = f"{base_url}?page={page_num}"
        page_data = scrape_page(page_url)
        if page_data:
            all_data.extend(page_data)
        else:
            break
    return all_data

base_url = 'https://example.com/data'
num_pages_to_scrape = 5
result = scrape_multiple_pages(base_url, num_pages_to_scrape)

for entry in result:
    print(entry.text)


