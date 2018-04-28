html_doc = """
<html>
  <head>
    <title>我是網頁標題</title>
    <style>
    .large {
      color:blue;
      text-align: center;
    }
    </style>
  </head>
  <body>
    <h1 class="large">我是變色且置中的抬頭</h1>
    <p id="p1">我是段落一</p>
    <p id="p2" style="">我是段落二</p>
    <div><a href='http://blog.castman.net' style="font-size:200%;">我是放大的超連結</a></div>
  </body>
</html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'html.parser')
print(soup)

paragraphs = soup.find_all('p')
print(paragraphs)
print(type(paragraphs))

for p in paragraphs:

    print(p['class'], p.text)

