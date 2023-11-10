from selenium.webdriver.common.by import By
from selenium import webdriver

import json

with open('./config.json', 'r') as f:
    config = json.load(f)

ID = config['LOTTO_KR']['ID']
PASS = config['LOTTO_KR']['PASS']
DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(DRIVER_PATH)

URL = 'https://dhlottery.co.kr/user.do?method=login&returnUrl='
driver.get(URL)

elem_login = driver.find_element(By.ID, 'userId')
elem_login.send_keys(ID)

elem_login = driver.find_element(By.NAME, "password")
elem_login.clear()
elem_login.send_keys(PASS)

LOGIN_XPATH = '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a'
driver.find_element(By.XPATH).click()