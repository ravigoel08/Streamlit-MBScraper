def dataCleaner(data: list)-> list:
    # Unit map
    Unit_map = {'sqft':1, 'sqm' : 10.7639, 'sqyrd': 9, 'Lac' : 100000, 'Cr' : 10000000}
    pack = []
    for i in range(1,len(data)):
        container = data[i].find("div",class_="clearfix")
        price = container.find("div", class_="m-srp-card__info flex__item").span
        area = container.find("div", class_="m-srp-card__summary__info")
        price = (price.text).split()
        area = (area.text).split()
        if area[1] == 'sqm' or area[1] == 'sqyrd':
            area[0] = area[0].replace(',','')
            area[0] = (float(area[0]))*Unit_map[f'{area[1]}']
        if price[1] == 'Cr' or price[1]=='Lac':
            price[0] = int((float(price[0]))*Unit_map[f'{price[1]}'])
        pack.append((area[0],price[0]))
    return pack