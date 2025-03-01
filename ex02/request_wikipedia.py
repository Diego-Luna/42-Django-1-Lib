import sys
import requests
import json
import dewiki
import re

def save_to_file(term, content):
    filename = re.sub(r'[^\w]', '_', term.lower()) + '.wiki'

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        # print(f"Content saved to {filename}")
        return True
    except:
        # print(f"Error: Could not save content to {filename}")
        return False

def get_wikipedia_page(search_query):
    url = "https://en.wikipedia.org/w/api.php"

    search_params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": search_query,
        "srlimit": 1  # Get only the best match
    }

    try:
        search_response = requests.get(url, params=search_params)
        search_response.raise_for_status()
        search_data = search_response.json()

        # * Check if we got search results
        if "query" in search_data and "search" in search_data["query"] and len(search_data["query"]["search"]) > 0:
            # * Get the title of the closest match
            page_title = search_data["query"]["search"][0]["title"]
            # print(f"Found article: '{page_title}'")
            
            # * Now fetch the full content of that page
            content_params = {
                "action": "query",
                "format": "json",
                "titles": page_title,
                "prop": "extracts",
                "explaintext": True,
                "redirects": True
            }
            
            content_response = requests.get(url, params=content_params)
            content_response.raise_for_status()
            content_data = content_response.json()
            
            # * Extract the page content
            pages = content_data["query"]["pages"]
            
            for page_id in pages:
                page = pages[page_id]
                
                # * Check if the page exists and return the content
                if "missing" not in page:
                    if "extract" in page and page["extract"]:
                        # Process Wiki markup
                        content = dewiki.from_string(page["extract"])
                        return content
            
            # No extract found
            print(f"No content found for '{search_query}'")
            return None
        else:
            # No search results
            print(f"No results found for '{search_query}'")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def main(search_query):
    # print("Starting request_wikipedia.py...")
    data = get_wikipedia_page(search_query)

    # print("\nContent:", data)

    if data is not None:
        save_to_file(search_query, data)
    else:
        print("No content to save.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 request_wikipedia.py <search_query>")
        sys.exit(1)
    main(sys.argv[1])