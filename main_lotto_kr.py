from selenium.webdriver.common.by import By
from selenium import webdriver

import json
from selenium.webdriver.chrome.options import Options


with open('./config.json', 'r') as f:
    config = json.load(f)

ID = config['LOTTO_KR']['ID']
PASS = config['LOTTO_KR']['PASS']
DRIVER_PATH = './chromedriver.exe'
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

URL = 'https://dhlottery.co.kr/user.do?method=login&returnUrl='
driver.get(URL)

elem_login = driver.find_element(By.ID, 'userId')
elem_login.send_keys(ID)

elem_login = driver.find_element(By.NAME, "password")
elem_login.clear()
elem_login.send_keys(PASS)

driver.execute_script("javascript:check_if_Valid3();")