import requests
from bs4 import BeautifulSoup

def parserlink(link):

	ibanez = requests.get(link)
	ibanez = ibanez.text

	soup = BeautifulSoup(ibanez,'lxml')

	page = soup.prettify()

	file2 = open('Ibanez_guitar_prettify.txt','w',encoding = 'UTF-8')
	file2.write(page)
	file2.close()
	return soup

	
def parseribanezlink(soup1):
	file1 = open('Ibanez_orginal_text.txt','w',encoding = 'UTF-8')

	findh1 = soup.find_all('img')
	linklist =[]
	for line in findh1:
		y = line.get('src')
		if y.startswith('images/'):
			y = 'http://www.ibanez.co.jp/products/' + y
			linklist.append(y)

	for i in linklist:
		file1.write(i+'\n')
	
	file1.close()
	return linklist

link1 = 'http://www.ibanez.co.jp/products/eg_top16_jp.php?year=2016&cat_id=1'
link2 = 'https://www.ptt.cc/bbs/Beauty/index.html'

soup = parserlink(link1)
link = parseribanezlink(soup)
