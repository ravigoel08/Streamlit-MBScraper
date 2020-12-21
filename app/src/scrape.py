from bs4 import BeautifulSoup
import requests
from . import constants
from typing import List
import streamlit as st
import time
from math import ceil


def mb_scraper(pages: int, cityname: str, property_type: str, bhk=1) -> List[str]:
    data = []
    pages = ceil(pages / 30)
    st.write("Scraping Progress")
    my_bar = st.progress(0)
    completion = 0
    for i in range(1, pages + 1):
        payload = {
            "proptype": f"{property_type}",
            "bedrooms": f"{bhk}",
            "cityName": f"{cityname}",
            "page": f"{i}",
        }
        req = requests.get(constants.URL, params=payload).content.decode("utf-8")
        soup = BeautifulSoup(req, "html.parser")
        data = data + soup.findAll("div", class_="SRCard")
        time.sleep(0.1)
        my_bar.progress((i - 1) / (pages - 1) if pages != 1 else 100)
    st.success("Completed") if len(data) != 0 else st.info("No Data to Scrape")
    return data
