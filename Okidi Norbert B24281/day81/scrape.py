import requests
from bs4 import BeautifulSoup

login_payload = {
    'username': 'okidi',
    'password': 'ball@556'
}

with open("login_page.html", "r", encoding="utf-8") as login_file:
    login_html = login_file.read()

with open("protected_page.html", "r", encoding="utf-8") as protected_file:
    protected_page_html = protected_file.read()


with requests.Session() as session:
    login_response = session.post("https://example.com/login", data=login_payload, headers={'Content-Type': 'text/html'}, cookies={'cookie_name': 'cookie_value'})

    if login_response.status_code == 200:
        scrape_response = session.get("https://example.com/protected-page", headers={'Content-Type': 'text/html'}, cookies={'cookie_name': 'cookie_value'})

        if scrape_response.status_code == 200:
            soup = BeautifulSoup(scrape_response.text, 'html.parser')

            paragraphs = soup.find_all('p')
            for paragraph in paragraphs:
                print(paragraph.get_text())
        else:
            print(f"Failed to access the protected page. Status code: {scrape_response.status_code}")
    else:
        print(f"Login failed. Status code: {login_response.status_code}")
