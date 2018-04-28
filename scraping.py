
from bs4 import BeautifulSoup
from urllib.request import urlopen3


html = urlopen("http://share.youthwant.com.tw/DP2014010.html")
print(html.read())

bsobj = BeautifulSoup(html.read(),"html.parser")

print("\n",bsobj)
