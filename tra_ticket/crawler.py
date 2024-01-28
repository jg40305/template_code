import sys
import time
import sqlite3
import csv
import json

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 瀏覽器配置
from selenium.webdriver.support.ui import WebDriverWait  # 等待工具
from selenium.webdriver.support import expected_conditions  # 預定義條件，供 WebDriverWait 使用
from selenium.webdriver.common.by import By  # 定位元素
# Selenium v4 compatible Code Block
# https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import chrome_helper
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


BASE_URL = "https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip123/query"  # 剩餘座位查詢

desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}


if __name__ == "__main__":
    chrome_service = Service()
    chrome_options = Options()
    # 隱藏 chrome 目前受到自動測試軟體控制
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-automation'])
    # 最大化視窗, 不載入圖片加速
    chrome_options.add_argument(
        '--start-maximized --blink-settings=imagesEnabled=false')
    # 模擬瀏覽器
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36'
    chrome_options.add_argument('user-agent={}'.format(user_agent))
    chrome_options.set_capability("goog:loggingPrefs",{"performance": "ALL"})

    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    browser.get(BASE_URL)

    start_station = "1000-臺北"
    end_station = "3300-臺中"
    start_time = "10:00"
    # end_time = "21:00"  # 最多只能查8小時區間
    id_num = "A123456789"

    WebDriverWait(browser, 30).until(
                expected_conditions.presence_of_element_located((By.ID, 'orderType1')))
    browser.maximize_window()

    actions = ActionChains(browser)

    with open('railway_test.html', 'w', encoding='utf-8') as fopen:
        fopen.write(browser.page_source)

    target_element = browser.find_element(By.ID, 'orderType2')
    actions.move_to_element(target_element)
    actions.click().perform()
    target_element = browser.find_element(By.ID, 'pid')
    target_element.send_keys(id_num)
    target_element = browser.find_element(By.ID, 'startStation1')
    target_element.send_keys(start_station)
    target_element = browser.find_element(By.ID, 'endStation1')
    target_element.send_keys(end_station)
    target_element = browser.find_element(By.ID, 'rideDate1')
    target_element.clear()
    target_element.send_keys("20240201")

    target_element = browser.find_element(By.ID, 'startTime1')
    select = Select(target_element)
    select.select_by_value(start_time)
    # # 最多只能查8小時區間
    # target_element = browser.find_element(By.ID, 'endTime1')
    # select = Select(target_element)
    # select.select_by_value(end_time)

    # 車種：自強3000，太魯閣，普悠瑪，自強，莒光，復興
    target_element = browser.find_element(By.ID, 'ticketOrderParamList0.trainTypeList1')
    actions.move_to_element(target_element)
    actions.click().perform()
    target_element = browser.find_element(By.ID, 'ticketOrderParamList0.trainTypeList2')
    actions.move_to_element(target_element)
    actions.click().perform()
    target_element = browser.find_element(By.ID, 'ticketOrderParamList0.trainTypeList3')
    actions.move_to_element(target_element)
    actions.click().perform()
    target_element = browser.find_element(By.ID, 'ticketOrderParamList0.trainTypeList4')
    actions.move_to_element(target_element)
    actions.click().perform()
    target_element = browser.find_element(By.ID, 'ticketOrderParamList0.trainTypeList5')
    actions.move_to_element(target_element)
    actions.click().perform()
    target_element = browser.find_element(By.ID, 'ticketOrderParamList0.trainTypeList6')
    actions.move_to_element(target_element)
    actions.click().perform()
    target_element = browser.find_element(By.CLASS_NAME, 'btn-sentgroup')
    target_element.submit()

    WebDriverWait(browser, 30).until(
                expected_conditions.presence_of_element_located((By.ID, 'rc-anchor-alert')))
    browser.maximize_window()
