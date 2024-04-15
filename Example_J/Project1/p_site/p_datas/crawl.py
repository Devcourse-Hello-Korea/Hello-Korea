from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

def set_dates_and_crawl(url, checkin_date, checkout_date):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get(url)

    date_click = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/input')
    date_click.click()

    checkin_input = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/input')
    checkin_input.click()
    checkin_input.send_keys(Keys.CONTROL, 'a')
    checkin_input.send_keys(Keys.BACK_SPACE)
    checkin_input.send_keys(checkin_date)
    checkin_input.send_keys(Keys.ENTER)

    checkout_input = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/input')
    checkout_input.click()
    checkout_input.send_keys(Keys.CONTROL, 'a')
    checkout_input.send_keys(Keys.BACK_SPACE)
    checkout_input.send_keys(checkout_date)
    checkout_input.send_keys(Keys.ENTER)

    start_element = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[4]/div/button[2]/span')
    start_element.click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[2]/div[2]/main/c-wiz/span/c-wiz/c-wiz[4]/div/a')))   
    first_element = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[2]/div[2]/main/c-wiz/span/c-wiz/c-wiz[4]/div/a')
    first_element.click()

    # 탭이 포함된 상위 div 선택
    tabs_container_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[1]/div/div/c-wiz/div/div[2]/div/div[2]'
    wait = WebDriverWait(driver, 10)
    tabs_container = wait.until(EC.presence_of_element_located((By.XPATH, tabs_container_xpath)))

    # 탭의 총 개수 파악
    tabs = tabs_container.find_elements(By.XPATH, './div')
    num_of_tabs = len(tabs)

    #for i in range(1, num_of_tabs + 1):
    for i in range(3, 10 + 3):
        # 탭 클릭
        tab_xpath = f'{tabs_container_xpath}/div[{i}]'
        wait = WebDriverWait(driver, 10)
        tab = wait.until(EC.visibility_of_element_located((By.XPATH, tab_xpath)))
        driver.execute_script("arguments[0].click();", tab)

        try:
            hotel_name = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[1]/div[1]/c-wiz/div/h1'))).text
        except NoSuchElementException:
            hotel_name = ""  # 호텔 이름이 없는 경우

        try:
            hotel_price = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[1]/div/section/div[1]/div[2]/c-wiz/div[1]/div/span/button/span/span[2]').text
        except NoSuchElementException:
            try:
                hotel_price = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[1]/div/section/div[1]/div[2]/c-wiz/div[1]/div/span/button/span/div[1]/span[3]/span').text
            except NoSuchElementException:
                hotel_price = "0"  # 호텔 가격이 없는 경우
        try:
            hotel_location = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[1]/div/section/div[1]/div[1]/div/div[2]/span').text
        except NoSuchElementException:
            hotel_location = ""  # 호텔 위치가 없는 경우

        hotel_price_int = convert_price_to_int(hotel_price)
        # Django 모델에 저장
        motel_info = MotelInfo(location=hotel_location, name=hotel_name, price=hotel_price_int)
        motel_info.save()

    driver.quit()

def convert_price_to_int(price_str):
    numeric_str = price_str.replace('₩', '').replace(',', '')
    return int(numeric_str)
