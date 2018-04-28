print("hello kiss my ass")
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://share.youthwant.com.tw/DP2014010.html")
print(html.read())

bsobj = BeautifulSoup(html.read(),"html.parser")

print("\n",bsobj.)

