import requests
from bs4 import BeautifulSoup

keyword = input('Keyword: ')

url = f'https://www.amazon.com/s/?ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={keyword}'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='s-results-list-atf')

items = results.find_all(class_='s-result-item')
# exclude class_='AdHolder'

for x in items:
	if x.find('h2'):
		name = x.find('h2').get_text()
	if x.find(class_='sx-price-large'):
		price = x.find(class_='sx-price-large').find(class_='sx-price-whole').get_text()+'.'+x.find(class_='sx-price-large').find(class_='sx-price-fractional').get_text()
	if x.find(class_='a-icon-star'):
		stars = x.find(class_='a-icon-star').find(class_='a-icon-alt').get_text()[:3]
	if x.find(class_='a-row').find('a', class_='a-size-small a-link-normal a-text-normal'):
		reviews = x.find(class_='a-row').find('a', class_='a-size-small a-link-normal a-text-normal').get_text()

	print(name)
	print(price)
	print(stars)
	print(reviews)
	print('')