import requests
from bs4 import BeautifulSoup
import sys

def google_search(query, num_results=5):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Send the request
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        
        # Extract search result blocks
        for g in soup.find_all('div', class_='tF2Cxc')[:num_results]:
            title = g.find('h3').text
            link = g.find('a')['href']
            results.append((title, link))
        
        return results
    else:
        print("Failed to retrieve search results.")
        return []

def main():
    if len(sys.argv) < 2:
        print("Usage: python google_terminal.py <search query>")
        sys.exit(1)
    
    query = ' '.join(sys.argv[1:])
    print(f"\nSearching Google for: '{query}'...\n")
    
    search_results = google_search(query)
    
    if search_results:
        for idx, (title, link) in enumerate(search_results, start=1):
            print(f"{idx}. {title}\n   {link}\n")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
