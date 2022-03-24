import requests
import bs4
from pprint import pprint

# url = 'https://2ip.ru'
#
# response = requests.get(url)
# response.raise_for_status()
#
# text = response.text
# soup = bs4.BeautifulSoup(text, features='html.parser')
# ip_address = soup.find(id='d_clip_button').find('span')
# print(ip_address.text)

url = 'https://habr.com'

HEADERS = {'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': '_ym_uid=1647686996580340397; _ym_d=1647686996; habr_web_home_feed=/all/; hl=ru; fl=ru; _ym_isad=2',
        'Host': 'habr.com',
        'If-None-Match': 'W/"633-9JRCHn+YSqMdA/AYP9kKu7S24X0"',
        'Referer': 'https://habr.com/ru/all/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Opera";v="84"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.42',
        'x-app-version': '2.67.0'}

response = requests.get(url, headers=HEADERS)
response.raise_for_status()

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    title = article.find(class_="tm-article-snippet__title-link").text
    link = article.find(class_="tm-article-snippet__title-link").attrs['href']
    text = article.find_all(class_="article-formatted-body article-formatted-body_version-2")

    for el in text:
        for word in KEYWORDS:
            if word in el.text.lower():
                print(article.find('time').text, '-', title, '-', url[0:16] + link)
