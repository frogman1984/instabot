from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# This script is about web scrapping
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\peterquinn\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
browser = webdriver.Chrome(".venv\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe", chrome_options=options)

browser.get('https://www.instagram.com/')
sleep(5)


username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("trip2ikigai")
password_input.send_keys("g0l0ndr1na")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(10)

browser.close()
