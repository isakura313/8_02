from bs4 import BeautifulSoup
with open('index.html') as html_doc:
    content = html_doc.read()
    print(content)


soup = BeautifulSoup(content, 'html.parser')

print(soup.title)

print(soup.title.string)
# контент нашего title
# print(soup.title.parent)

print(soup.p.string)
print(soup.p['class'])
print(soup.a['href'])

print(soup.find_all('a'))
spi_bs4 = soup.find_all('a')
for i in spi_bs4:
    print(i['href'])
