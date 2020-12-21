from src import *
import streamlit as st
import pandas as pd
import time
import json


def main():
    st.title("Streamlit-MBScraper")
    cityname = st.sidebar.selectbox("Select City Name", constants.STATE)
    property_type = st.sidebar.multiselect("Select Properties Type", constants.PROPERTY)
    property_type = ','.join(property_type)
    bhk = st.sidebar.slider("BHK", 1, 4, 1, 1)
    validate = st.sidebar.checkbox("Check Data Availability")
    if validate:
        data = page.total_page(cityname, property_type, bhk)
        st.sidebar.write(data)
    add_scrapebutton = st.sidebar.checkbox("Start Scraping")
    if add_scrapebutton:
        scraped_data = scrape.mb_scraper(data, cityname, property_type,bhk)
        cleandata = cleaner.data_cleaner(scraped_data, data)
        df = pd.DataFrame(cleandata, columns=constants.COLUMNS)
        if not df.empty:
            tmp_download_link = export.export_csv(df)
            st.markdown(tmp_download_link, unsafe_allow_html=True)
            st.json(df.to_json(orient="records"))


if __name__ == "__main__":
    main()
