import requests
from bs4 import BeautifulSoup

keywords = list(map(str, input("Search for: ").upper().split())) 		#Ключевые слова

resp = requests.get('https://us.bape.com/sitemap_products_1.xml')
txt = resp.text
soup = BeautifulSoup(txt, features='lxml')

imgTitleList = soup.find_all('image:title')								#Список с названиями

for item in imgTitleList:
	var = item.text.split(' ')
	result = list(set(keywords) & set(var))
	if result != []:
		parent = item.parent.parent
		print(parent.find('loc').text)
