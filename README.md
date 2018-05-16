# Context
I am interested in data analysis and wanted to try some scraping. Some friends of mine are avid investors and wanted to be able to see all the publicly available ASX options data in one place. I built this scraper to put that information together.

# What is ASX Scraper?
This tool allows you to create a CSV file that contains the publicly available options data for all ASX traded options. Essentially, it generates a snapshot-in-time spreadsheet of all ASX traded options.

# How to use ASX Scraper
1. Clone the repository onto your computer
2. Install Scrapy with `pip install Scrapy`
4. Install bs4 with `pip install beautifulsoup4`
5. `cd` into /asxscrape and run `python -m scrapy crawl asx_spider`. This will create a .html file in /asxscrape for every company that has ASX traded options. About 100 .html files will be generated.
6. Run `python parser.py` from /asxscrape. parser.py will create a new CSV file, parse through the .html files one by one, extract the options data, and place the data into the CSV file.
7. Copy-paste the data from the CSV file into a MS Excel spreadsheet.