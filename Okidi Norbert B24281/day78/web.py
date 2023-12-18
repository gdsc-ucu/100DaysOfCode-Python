from bs4 import BeautifulSoup


with open("web.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
links = soup.find_all('a')

for link in links:
    print(link.get('href'))