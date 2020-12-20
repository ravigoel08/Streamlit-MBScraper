from bs4 import BeautifulSoup
import requests
from . import constants
from typing import List


def mb_scraper(pages: int, cityname: str, bhk=1) -> List[str]:
    data = []
    for i in range(1, pages):
        print("page " + f"{i}" + " scraped")
        payload = {
            "proptype": f"{constants.PROPERTY}",
            "bedrooms": f"{bhk}",
            "cityName": f"{cityname}",
            "page": f"{i}",
        }
        req = requests.get(constants.URL, params=payload).content.decode("utf-8")
        soup = BeautifulSoup(req, "html.parser")
        data = data + soup.findAll("div", class_="SRCard")
    return data
