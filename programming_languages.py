import json
import re
import requests
from bs4 import BeautifulSoup


def get_language_list():
    source_url = "https://www.tiobe.com/tiobe-index/programminglanguages_definition/"
    css_selector = 'a[name="instances"] ~ ul > li'

    re_brackets = r'\(.*?\)'
    re_grouping = r'^.*?:'

    try:
        languages = set()

        response = requests.get(source_url)
        response.raise_for_status()  # Check if the request was successful

        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.select(css_selector)

        for li in elements:
            txt = re.sub(re_brackets, '', li.text)
            txt = re.sub(re_grouping, '', txt)
            
            for entry in txt.split(','):
                languages.add(entry.strip())

        return sorted(languages)

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving the URL: {e}")
        return None
    
if __name__ == "__main__":
    langlist = get_language_list()
    
    with open('languages.txt', 'w') as fh:
        for lang in langlist:
            fh.write(f"{lang}\n")
    
    with open('languages.json', 'w') as fh:
        json.dump(langlist, fh)
    
    