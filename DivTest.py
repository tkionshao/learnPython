html = '''
<div>6666</div>
'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
page = soup.prettify()
