import urllib.request as url
import bs4
# import warnings

# warnings.filterwarnings("ignore")

path = "https://www.flipkart.com/search?q=iphone+11"
response = url.urlopen(path)

page = bs4.BeautifulSoup(response,'html.parser')
# title = page.find('div', attrs={'class' : "_4rR01T"})

title = page.find('div', class_='_4rR01T')
print(title.text)

price = page.find('div', class_='_30jeq3 _1_WHN1')
print(price.text)