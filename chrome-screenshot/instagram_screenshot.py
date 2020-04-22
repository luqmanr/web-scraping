import os, sys, time, errno, cv2, pickle, getpass
from optparse import OptionParser
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from tqdm import tqdm

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1440,2560"

sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

driver = webdriver.Chrome(
    executable_path="/usr/lib/chromium-browser/chromedriver",
    chrome_options=chrome_options
)

def InstagramCrawler(keyword, out_path):
    # driver.get("https://www.instagram.com/accounts/login/")
    # time.sleep(5)

    # cookies = loginInstagram(keyword)
    cookies = None
    # ProfileScreenshot(keyword, out_path, cookies)
    # PhotoDownloader(keyword, out_path, cookies)
    PostFinder(keyword, out_path, cookies)
    driver.close()

def loginInstagram(keyword):
    login_id = input('Username Akun Instagram Anda: ')
    password = getpass.getpass('Password Akun Instagram Anda: ')

    try:
        username_bar = driver.find_element_by_name("username")
        username_bar.send_keys(login_id)
        print('username inserted')

        password_bar = driver.find_element_by_name("password")
        password_bar.send_keys(password)
        print('password inserted')

        time.sleep(2)

        login_button = driver.find_element_by_class_name("L3NKy")
        login_button.click()
        print('logging in')
    
    except:
        print(" ")
        print("LOG IN FAILED")
        pass

    time.sleep(5)

    user_profile_xpath = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a'
    try:
        check_logged_in = driver.find_element_by_xpath(user_profile_xpath)
        if check_logged_in:
            print(" ")
            print("LOG IN SUCCESS")
    except:
    # check_logged_in = driver.find_element_by_class_name("L3NKy")
        print(" ")
        print("LOG IN FAILED")
    

    cookies = driver.get_cookies()
    for cookie in cookies:
        if 'expiry' in cookie:
            cookie['expiry'] = int(cookie['expiry'])

    return cookies
    
def ProfileScreenshot(keyword, out_path, cookies):
    instagram_url = "https://www.instagram.com/"
    keywords_link = instagram_url + keyword
    if not keywords_link.startswith('http'):
        raise Exception('URLs need to start with "http"') 

    print('opening page')

    driver.get(keywords_link)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

    time.sleep(5)

    scroll_iterator = 0
    height = 0
    for i in range(100):
        next_height = driver.execute_script("return document.body.scrollHeight")

        if next_height == height:
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
        print('making Instagram screenshots for', keyword, (i+1))
        driver.save_screenshot(os.path.join(save_path, str(timestamp)+'.png'))
        driver.execute_script("window.scrollBy(0,2160)")
        time.sleep(3)
        scroll_iterator += 1

def PhotoDownloader(keyword, out_path, cookies):
    instagram_url = "https://www.instagram.com/"
    keywords_link = instagram_url + keyword
    if not keywords_link.startswith('http'):
        raise Exception('URLs need to start with "http"') 

    print('opening page')

    driver.get(keywords_link)

    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

    time.sleep(5)

    def ScrapeLinks():
        scroll_iterator = 0
        height = 0
        link_list = []

        for i in range(10):
            try:
                photo_elements = driver.find_elements_by_class_name('FFVAD')

                for photos in photo_elements:
                    link_list.append(photos.get_attribute('src'))

                next_height = driver.execute_script("return document.body.scrollHeight")
                if next_height == height:
                    break
                height = driver.execute_script("return document.body.scrollHeight")

                driver.execute_script("window.scrollBy(0,2160)")
                time.sleep(3)
                scroll_iterator += 1
            except:
                pass
        link_list = list(dict.fromkeys(link_list))
        print(link_list)
        return link_list
    
    def OpenLinks():
        for index, links in enumerate(link_list):
            driver.get(links)

            time.sleep(2)

            save_path = os.path.join(out_path, keyword)
            try:
                os.makedirs(save_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            print('making Instagram screenshots for', keyword, (index+1))
            driver.save_screenshot(os.path.join(save_path, str(timestamp)+'.png'))

    link_list = ScrapeLinks()
    OpenLinks()

def PostFinder(keyword, out_path, cookies):
    instagram_url = "https://www.instagram.com/"
    keywords_link = instagram_url + keyword
    if not keywords_link.startswith('http'):
        raise Exception('URLs need to start with "http"') 

    print('opening', keyword, 'page')

    driver.get(keywords_link)
    try:
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
    except:
        print('no cookies')

    time.sleep(5)

    def ScrapeLinks():
        scroll_iterator = 0
        height = 0
        link_list = []

        for i in range(20):
            try:
                driver.execute_script("window.scrollBy(0,2160)")
                time.sleep(3)
                more_posts = driver.find_elements_by_class_name('tCibT')
                for button in more_posts:
                    button.click()
            except:
                print('no "more posts" button found')
            try:
                photo_elements = driver.find_elements_by_tag_name('a')

                for photos in photo_elements:
                    post_link = str(photos.get_attribute('href'))

                    if '/p/' in post_link:
                        link_list.append(post_link)
                        # print(post_link, 'appended to links', '\n')

                next_height = driver.execute_script("return document.body.scrollHeight")
                if next_height == height:
                    break
                height = driver.execute_script("return document.body.scrollHeight")

                driver.execute_script("window.scrollBy(0,2160)")
                time.sleep(3)
                scroll_iterator += 1
            except:
                pass
        link_list = list(dict.fromkeys(link_list))
        print(len(link_list), "photos found")
        return link_list
    
    def OpenLinks():
        for index, links in enumerate(link_list):
            driver.get(links)

            time.sleep(2)

            save_path = os.path.join(out_path, keyword)
            try:
                os.makedirs(save_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            print('making Instagram screenshots for', keyword, (index+1))
            driver.save_screenshot(os.path.join(save_path, str(timestamp)+'.png'))

    link_list = ScrapeLinks()
    OpenLinks()
    time.sleep(5)