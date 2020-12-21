import requests
from . import constants
from bs4 import BeautifulSoup


def total_page(cityname: str, property_type: str, bhk=1) -> int:
    pages = 0
    payload = {
        "proptype": property_type,
        "bedrooms": f"{bhk}",
        "cityName": cityname,
    }
    req = requests.get(constants.URL, params=payload).content.decode("utf-8")
    soup = BeautifulSoup(req, "html.parser")
    container = soup.find("div", class_="headingNFilter")
    result = container.find("div", class_="SRHeadingPar")
    if result:
        result = result.h1
        pages = int(result.text.split()[0])
    return pages
