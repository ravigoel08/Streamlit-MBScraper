from src import *

if __name__ == '__main__':
    data = scrape.mbscraper(100)
    cleandata = cleaner.dataCleaner(data)
    export.exportCsv(cleandata)