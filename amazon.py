import requests
import pandas
import datetime
from bs4 import BeautifulSoup

keyword = input('Keyword: ')
time = datetime.datetime.now().strftime('%I%M%p%d%B')
filename = f'./{keyword}{time}.csv'

url = f'https://www.amazon.com/s/?ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={keyword}'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='s-results-list-atf')

items = results.find_all(class_='s-result-item')
# exclude class_='AdHolder'

names = []
prices = []
stars = []
reviews = []

for item in items:

	if item.find('h2'):
		name = item.find('h2').get_text()
		names.append(name)
	if item.find(class_='sx-price-large'):
		price = item.find(class_='sx-price-large').find(class_='sx-price-whole').get_text()+'.'+item.find(class_='sx-price-large').find(class_='sx-price-fractional').get_text()
		prices.append(price)
	if item.find(class_='a-icon-star'):
		star = str(item.find(class_='a-icon-star').find(class_='a-icon-alt').get_text()[:3])
		stars.append(star)
	'''if item.find(class_='a-row').find('a', class_='a-size-small a-link-normal a-text-normal'):
		review = item.find(class_='a-row').find('a', class_='a-size-small a-link-normal a-text-normal').get_text()
		reviews.append(review)
'''
df = pandas.DataFrame(data={"Name": names, "Price": prices, "Stars": stars})
df.to_csv(filename, sep=',',index=False)