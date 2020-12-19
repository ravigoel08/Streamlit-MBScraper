from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def mbscraper(pages: int):
    data = []
    #fetching Container containing the data required by looping through each page
    
    for i in range(1, pages):
        print('page ' +f'{i}'+' scraped')
        my_url = f"https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Residential-House,Villa&cityName=New-Delhi&page={i}"
        req = Request(my_url, headers={'User-Agent':'Mozilla/5.0'})
        uClient = urlopen(req).read()
        ucl = uClient.decode('utf-8')
        soup = BeautifulSoup(ucl,"html.parser")
        data = data + soup.findAll("div",class_="SRCard")
    return data