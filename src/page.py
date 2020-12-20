import requests
from . import constants
from bs4 import BeautifulSoup


def total_page(cityname: str, bhk=1) -> int:
    pages = 0
    payload = {
        "proptype": f"{constants.PROPERTY}",
        "bedrooms": f"{bhk}",
        "cityName": f"{cityname}",
    }
    req = requests.get(constants.URL, params=payload).content.decode("utf-8")
    soup = BeautifulSoup(req, "html.parser")
    container = soup.find("div", class_="headingNFilter")
    result = container.find("div", class_="SRHeadingPar").h1
    if result:
        pages = int(result.text.split()[0]) // 30
    return (pages,)
