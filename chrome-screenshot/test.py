import os, time, errno, sys
from datetime import datetime
from optparse import OptionParser
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1280,720"

chrome_options = Options()  
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

def BingCrawler(keyword, out_path):
    driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH,
        options=chrome_options
    ) 

    bing_url = "https://www.bing.com/images/search?q="
    keywords_link = bing_url + keyword
    # fullScreenshot(keywords_link, keyword, driver, out_path)
    focusedScreenshot(keywords_link, keyword, driver, out_path)

    driver.close()

def fullScreenshot(keywords_link, keyword, driver, out_path):
    if not keywords_link.startswith('http'):
        raise Exception('URLs need to start with "http"') 

    print('opening page')
    driver.get(keywords_link)

    scroll_iterator = 0
    height = 0
    for i in range(10):
        next_height = driver.execute_script("return document.body.scrollHeight")

        if next_height == height:
            time.sleep(3)
            # break
            try:
                driver.execute_script("window.scrollBy(0,1080)")
                time.sleep(3)
                
                find_more = driver.find_element_by_class_name("btn_seemore")
                find_more.click()
                print("find more clicked")

                time.sleep(3)

            except:
                print("reached end of page")
                break

        height = driver.execute_script("return document.body.scrollHeight")

        save_path = os.path.join(out_path, keyword)
        try:
            os.makedirs(save_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        print('making Bing screenshots for', keyword, (i+1))
        driver.save_screenshot(os.path.join(save_path, str(timestamp)+'.png'))
        driver.execute_script("window.scrollBy(0,1920)")
        time.sleep(5)
        scroll_iterator += 1

def focusedScreenshot(keywords_link, keyword, driver, out_path):
    if not keywords_link.startswith('http'):
        raise Exception('URLs need to start with "http"') 

    print('opening page')
    driver.get(keywords_link)

    time.sleep(2)

    scroll_iterator = 0
    height = 0

    # num_photos = 
    def findPhotoLinks():
        try:
            Hrefs = driver.find_elements_by_class_name('iusc')
            for index, href in enumerate(Hrefs):
                if index == 0:
                    return href, len(Hrefs)
        except:
            print('first link not found')
            return None

    firstPhoto, num_photos = findPhotoLinks()
    firstPhoto.click()

    time.sleep(3)

    photo_limit = num_photos * 4
    retry_count = 0
    retry_limit = 5

    for i in range(photo_limit):
        save_path = os.path.join(out_path, keyword)
        try:
            os.makedirs(save_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        if i == 0:
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            print('making Bing screenshots for', keyword, (i+1))
            driver.save_screenshot(os.path.join(save_path, str(timestamp)+'.png'))

            print('screenshot made')
            time.sleep(2)
        
        if i == 1:
            sys.exit()

        try:
            actions = ActionChains(driver)
            actions.send_keys(Keys.ARROW_RIGHT).perform()

            # right_button = driver.get_elements_by_class_name('nav')
            # print(right_button)
        except:
            print('no photos found')
            retry_count += 1

        if retry_count == retry_limit:
            print('no more photos found')
            break
        
        time.sleep(2)

        now = datetime.now()
        timestamp = datetime.timestamp(now)
        print('making Bing screenshots for', keyword, (i+2))
        driver.save_screenshot(os.path.join(save_path, str(timestamp)+'.png'))

driver = webdriver.Chrome(
    executable_path=CHROMEDRIVER_PATH,
    options=chrome_options
) 

bing_url = "https://www.bing.com/images/search?q="
keyword = 'ash ortega filipina'
keywords_link = bing_url + keyword
focusedScreenshot(keywords_link, keyword, driver, out_path="none")