from . import constants
from typing import List


def data_cleaner(data: List[str], result: int):
    pack = []
    for i in range(0, result):
        container = data[i].find("div", class_=constants.CONTAINER)
        price = container.find("div", class_=constants.PRICE).span
        area = container.find("div", class_=constants.AREA)
        apartment = container.find("span", class_=constants.APARTMENT)
        location = container.find("span", class_=constants.LOCATION)
        address = " ".join(location.text[location.text.find("in") + 2 :].split())
        bhk = apartment.text.split()[0]
        appartment_type = " ".join(apartment.text.split()[1:])
        price = (price.text).split()
        area = (area.text).split()
        if area[1] == "sqm" or area[1] == "sqyrd":
            area[0] = area[0].replace(",", "")
            area[0] = (float(area[0])) * constants.UNIT_MAP[f"{area[1]}"]
        if price[1] == "Cr" or price[1] == "Lac":
            price[0] = int((float(price[0])) * constants.UNIT_MAP[f"{price[1]}"])
        pack.append((area[0], price[0], address, bhk, appartment_type))
    return pack
