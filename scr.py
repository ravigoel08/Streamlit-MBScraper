from bs4 import BeautifulSoup
from urllib.request import Request, urlopen 
a = []
#unit map for unit coversion 
Unit_map = {'sqft':1, 'sqm' : 10.7639, 'sqyrd': 9, 'Lac' : 100000, 'Cr' : 10000000}
#external File
outfile_name = 'data.csv'
#CSV headers
headers = 'Price, Area'
f = open(outfile_name,'w')
f.write(headers)

#fetching Container containing the data required by looping through each page
for i in range(1,104):
    print('page ' +f'{i}'+' scraped')
    my_url = f"https://www.magicbricks.com/mbsearch/propertySearch.html?propertyType_new=10001_10017&city=2624&searchType=1&propertyType=10001,10017&disWeb=Y&pType=10001,10017&category=S&groupstart=90&offset=0&maxOffset=4&attractiveIds=&page={i}&ltrIds=&preCompiledProp=&excludePropIds=&addpropertyDataSet="
    req = Request(my_url, headers={'User-Agent':'Mozilla/5.0'})
    uClient = urlopen(req).read()
    ucl = uClient.decode('utf-8')
    soup = BeautifulSoup(ucl,"html.parser")
    a = a + soup.findAll("div",class_="SRCard")

#total data    
print(len(a))  

#creating CSV
for i in range(1,len(a)):
    container = a[i].find("div",class_="clearfix")
    price = container.find("div", class_="m-srp-card__info flex__item").span
    area = container.find("div", class_="m-srp-card__summary__info")
    price = (price.text).split()
    area = (area.text).split()
    if area[1] == 'sqm' or area[1] == 'sqyrd':
        area[0] = str((int(area[0]))*Unit_map[f'{area[1]}'])
    if price[1] == 'Cr' or 'Lac' :
        price[0] = (str(int(float(price[0]))*Unit_map[f'{price[1]}']))
    f.write(price[0] + ", " + area[0] + "\n")
f.close()
