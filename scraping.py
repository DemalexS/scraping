import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'web', 'deep']

resp = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(resp.text, 'html.parser')
posts = soup.find_all('article', class_='post')

for post in posts:

    title = post.find('a', class_='post__title_link')
    date = post.find('span', class_='post__time')
    href = title.attrs.get('href')

    hubs = post.find_all('a', class_='hub-link')

    post_text = post.find('div', class_='post__text')
    text = post_text.text.lower()
    for keyword in KEYWORDS:
        for hub in hubs:
            hub_lower = hub.text.lower()

            if keyword in text or keyword in title.text.lower() or keyword in hub_lower:
                print(f'{date.text} - {title.text} - {href}')
                break
