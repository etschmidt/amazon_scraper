import requests
from bs4 import BeautifulSoup

keyword = input('Keyword: ')

url = f'https://www.amazon.com/s/?ref=nb_sb_noss_2?url=search-alias%3Dhpc&field-keywords={keyword}'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='s-results-list-atf')

items = results.find_all(class_='s-result-item')
# exclude class_='AdHolder'

for x in items:
	name = x.find('h2').get_text()
	price = x.find(class_='sx-price-large').get_text()
	stars = x.find(class_='a-icon-alt').get_text()
	reviews = x.find(class_='a-size-small a-link-normal a-text-normal').get_text()

	print(name)
	print(price)
	print(stars)
	print(reviews)
	print('')