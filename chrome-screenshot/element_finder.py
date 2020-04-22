import os, time, errno, pickle, stdiomask, getpass, sys
from selenium import webdriver
import selenium
import re
from urllib.request import urlopen
import json
import csv
import yaml

## IF LINUX USE THIS
CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1440,2560"

sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome(
    executable_path="/usr/lib/chromium-browser/chromedriver",
    chrome_options=chrome_options
)

url_page = "https://www.ranker.com/list/famous-people-from-cambodia/reference"

name_xpath1 = "/html/body/article/div[%i]/div/a"
name_xpath2 = '/html/body/article/div[%i]/div/span[1]'

driver.get(url_page)

time.sleep(3)



scroll_iterator = 0
height = 0
for i in range(10):
    next_height = driver.execute_script("return document.body.scrollHeight")

    if next_height == height:
        # time.sleep(3)
        try:
            driver.execute_script("window.scrollBy(0,2560)")

        except:
            # name_tag = driver.find_element_by_xpath(name_xpath %i)
            # print(name_tag.text)
            print("reached end of page")
            break

    height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollBy(0,2560)")

    scroll_iterator += 1

# for i in range(170):
try:
    # print(name_xpath %i)
    # name_tag1 = driver.find_element_by_xpath(name_xpath1 %i)
    # print(name_tag1.text)
    # name_tag2 = driver.find_element_by_xpath(name_xpath2 %i)
    # print(name_tag1.text)
    name_tag3 = driver.find_elements_by_class_name("listItem__title")
    for texts in name_tag3:
        print(texts.text)
except:
    pass
        # print('done')