from src import *

if __name__ == "__main__":
    cityname = "New-Delhi"
    bhk = 1
    pages = page.total_page(cityname, bhk)
    data = scrape.mb_scraper(pages, cityname, bhk)
    cleandata = cleaner.data_cleaner(data)
    export.export_csv(cleandata, "export.csv")
