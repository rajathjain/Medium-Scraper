from bs4 import BeautifulSoup
import re
import pandas as pd
import requests
import unicodedata


def scrape_story(url):
        page_response = requests.get(url, timeout=15)
        page_content = BeautifulSoup(page_response.content, "html.parser")
        divs = page_content.find_all('div', {'class' : 'section-inner sectionLayout--insetColumn'})
        content =' '.join( [ div.get_text(strip=True) for div in divs ])
        content = unicodedata.normalize("NFKD", content)
        return content
        