from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import json
from selenium.webdriver.chrome.options import Options

#
# with open('./config.json', 'r') as f:
#     config = json.load(f)
#
# ID = config['LOTTO_KR']['ID']
# PASS = config['LOTTO_KR']['PASS']
# DRIVER_PATH = './chromedriver.exe'
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)
#
# URL = 'https://dhlottery.co.kr/user.do?method=login&returnUrl='
# driver.get(URL)
#
# elem_login = driver.find_element(By.ID, 'userId')
# elem_login.send_keys(ID)
#
# elem_login = driver.find_element(By.NAME, "password")
# elem_login.clear()
# elem_login.send_keys(PASS)
#
# driver.execute_script("javascript:check_if_Valid3();")
# LOTTO_BUY_URL = 'https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40'
# driver.get(LOTTO_BUY_URL)

pos_1_list = [1,2,3,4,5]
pos_2_list = [7,8,10,11,12]
pos_3_list = [13,15,19,18,20]
pos_4_list = [24,26,27,31,33]
pos_5_list = [34,36,37,38,39]
pos_6_list = [40,42,43,44,45]

result_list = []

result_list.append(random.sample(pos_1_list, 1)[0])

is_in_result = True
while is_in_result:
    pos2 = random.sample(pos_2_list, 1)[0]
    if pos2 not in result_list:
        result_list.append(pos2)
        is_in_result = False

is_in_result = True
while is_in_result:
    pos2 = random.sample(pos_3_list, 1)[0]
    if pos2 not in result_list:
        result_list.append(pos2)
        is_in_result = False

is_in_result = True
while is_in_result:
    pos2 = random.sample(pos_4_list, 1)[0]
    if pos2 not in result_list:
        result_list.append(pos2)
        is_in_result = False

is_in_result = True
while is_in_result:
    pos2 = random.sample(pos_5_list, 1)[0]
    if pos2 not in result_list:
        result_list.append(pos2)
        is_in_result = False

is_in_result = True
while is_in_result:
    pos2 = random.sample(pos_6_list, 1)[0]
    if pos2 not in result_list:
        result_list.append(pos2)
        is_in_result = False
print(result_list)