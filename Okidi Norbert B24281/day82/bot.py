import requests
from bs4 import BeautifulSoup
import time

def check_website_for_updates():
    url = "https://example.com"
    previous_data = None

    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            current_data = soup.get_text()

            if current_data != previous_data:
                print("Website has been updated!")

  
            previous_data = current_data

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

            time.sleep(3600)
check_website_for_updates()