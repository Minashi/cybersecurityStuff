import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.wikipedia.org/').read()
soup = bs.BeautifulSoup(source, 'html')
print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)
print(soup.p)
