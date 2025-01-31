# import selenium
from selenium import webdriver

# import time library
import time

# initialize a formatted url to feed into a loop to scrape data

# initialize selenium for Google Chrome
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome()

# initialize a year range to scrape rookie stats for a given year
years = list(range(1980, 2026))

# initialize a formatted url to feed into a loop to scrape data
rookies_url = "https://www.basketball-reference.com/leagues/NBA_{}_rookies-season-stats.html"

# this loop will go through the year list and grab the html of that page and save it to a folder called rookies
for year in years:
    url = rookies_url.format(year)
    driver.get(url)
    driver.execute_script("window.scrollTo(1,10000)")
    time.sleep(5)
    html = driver.page_source

    with open(".../rookies/rookie_stats_{}.html".format(year), "w+", encoding="utf-8") as f:
        f.write(html)