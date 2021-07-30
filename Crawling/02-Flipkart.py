import urllib.request as url
import bs4

path = "https://www.flipkart.com/search?q=iphone+11"
response = url.urlopen(path)

page = bs4.BeautifulSoup(response,'html.parser')

titleList = page.find_all('div', class_='_4rR01T')
priceList = page.find_all('div', class_='_30jeq3 _1_WHN1')

for i in range(len(titleList)):
    print(titleList[i].text)
    print(priceList[i].text)
    print("*" * 20)