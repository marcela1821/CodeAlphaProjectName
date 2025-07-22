import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title else "Brak tytułu"
        print(f"Title of {url}: {title}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Test 
get_page_title("https://www.vogue.pl/")
