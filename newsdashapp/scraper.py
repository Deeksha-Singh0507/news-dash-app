import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = 'https://news.ycombinator.com/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select('.titleline a')

    news = []
    for title in titles:
        news.append({
            'title': title.get_text(),
            'link': title['href']
        })

    return news
