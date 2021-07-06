import requests
# from bs4 import BeautifulSoup
import re

def searcher(query):
    search_url = 'https://www.youtube.com/results?search_query='+query
    r = requests.get(search_url)
    video_ids = re.findall(r"watch\?v=(\S{11})", r.text)

    return video_ids

if __name__=='__main__':
    searcher()