from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
'''
import jieba
from wordcloud import WordCloud
'''
rss_site = "https://tw.appledaily.com/rss/newcreate/kind/rnews/type/104"

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': 1
}

req = Request(rss_site, headers=hdr)
xml = urlopen(req)
bs = BeautifulSoup(xml.read(), "lxml")

# find all hyper-links
a = bs.findAll('a')

# get all articles
articles = []
for link in a:
    if 'href' in link.attrs:
        article_url = link.attrs["href"]
        print(article_url)
        html = urlopen(article_url)
        article = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        p = article.find('p')
#        print(p)
        articles.append(p)

print(articles)
'''
XPath
    from lxml import etree
    
    selector = etree.HTML(html)
    links = selector.xpath('//h4/a/text()')
    for link in links:
    print link
'''
