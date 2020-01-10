from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def mbscraper():
    a = []
    #Number of available pages to scrape
    pages = 104
    #unit map for unit coversion 
    Unit_map = {'sqft':1, 'sqm' : 10.7639, 'sqyrd': 9, 'Lac' : 100000, 'Cr' : 10000000}
    #external File
    outfile_name = 'data.csv'
    #CSV headers
    headers = 'Price, Area'
    f = open(outfile_name,'w')
    f.write(headers)

    #fetching Container containing the data required by looping through each page
    for i in range(1, pages):
        print('page ' +f'{i}'+' scraped')
        my_url = f"https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Residential-House,Villa&cityName=New-Delhi&page={i}"
        req = Request(my_url, headers={'User-Agent':'Mozilla/5.0'})
        uClient = urlopen(req).read()
        ucl = uClient.decode('utf-8')
        soup = BeautifulSoup(ucl,"html.parser")
        a = a + soup.findAll("div",class_="SRCard")

    #creating CSV
    for i in range(1,len(a)):
        container = a[i].find("div",class_="clearfix")
        price = container.find("div", class_="m-srp-card__info flex__item").span
        area = container.find("div", class_="m-srp-card__summary__info")
        price = (price.text).split()
        area = (area.text).split()
        if area[1] == 'sqm' or area[1] == 'sqyrd':
            area[0] = area[0].replace(',','')
            area[0] = (float(area[0]))*Unit_map[f'{area[1]}']
        if price[1] == 'Cr' or price[1]=='Lac':
            price[0] = int((float(price[0]))*Unit_map[f'{price[1]}'])
        f.write(str(price[0]) + ", " + str(area[0]) + "\n")
    f.close()

if __name__ == "__main__" :
    mbscraper()
