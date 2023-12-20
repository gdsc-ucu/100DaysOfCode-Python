from bs4 import BeautifulSoup
import pandas as pd

with open("website.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')

data = []
for row in table.find_all('tr'):
    row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
    data.append(row_data)

df = pd.DataFrame(data[1:], columns=data[0])

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

df.to_csv("cleaned_data.csv", index=False)

print("Cleaning and saving to CSV complete.")