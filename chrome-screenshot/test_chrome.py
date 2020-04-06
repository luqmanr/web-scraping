import time, os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(chrome_options=chrome_options)  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(1) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
driver.save_screenshot('./TEST.png')
time.sleep(1) # Let the user actually see something!
driver.quit()