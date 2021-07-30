import urllib.request as url
import bs4

for page_number in range(1,4):
    print(f"Fetching data from page {page_number}")
    path = f"https://www.flipkart.com/search?q=iphone+11&page={page_number}"
    response = url.urlopen(path)

    page = bs4.BeautifulSoup(response,'html.parser')

    titleList = page.find_all('div', class_='_4rR01T')
    priceList = page.find_all('div', class_='_30jeq3 _1_WHN1')

    for i in range(len(titleList)):
        print(titleList[i].text)
        print(priceList[i].text)
        print("*" * 20)