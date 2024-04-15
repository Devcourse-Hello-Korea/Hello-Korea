from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .accomodation_models import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

def date_inputs(driver, path, date):
    date_input = driver.find_element(By.XPATH, path)
    date_input.click()
    date_input.send_keys(Keys.CONTROL, 'a')
    date_input.send_keys(Keys.BACK_SPACE)
    date_input.send_keys(date)
    date_input.send_keys(Keys.ENTER)

def process_accomodation_tab(driver, tabs_container_xpath):
    wait = WebDriverWait(driver, 10)
    tabs_container = wait.until(EC.presence_of_element_located((By.XPATH, tabs_container_xpath)))
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
            accomodation_name = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[1]/div[1]/c-wiz/div/h1'))).text
        except NoSuchElementException:
            accomodation_name = ""  # 호텔 이름이 없는 경우

        try:
            accomodation_price = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[1]/div/section/div[1]/div[2]/c-wiz/div[1]/div/span/button/span/span[2]').text
        except NoSuchElementException:
            try:
                accomodation_price = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[1]/div/section/div[1]/div[2]/c-wiz/div[1]/div/span/button/span/div[1]/span[3]/span').text
            except NoSuchElementException:
                accomodation_price = "0"  # 호텔 가격이 없는 경우
        try:
            accomodation_location = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[1]/div/section/div[1]/div[1]/div/div[2]/span').text
        except NoSuchElementException:
            accomodation_location = ""  # 호텔 위치가 없는 경우

        accomodation_price_int = convert_price_to_int(accomodation_price)
        # Django 모델에 저장
        accomodation_info = AccomodationInfo(location=accomodation_location, name=accomodation_name, price=accomodation_price_int)
        accomodation_info.save()

def set_dates_and_crawl(url, checkin_date, checkout_date):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get(url)
    date_click_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/input'
    date_click = driver.find_element(By.XPATH, date_click_xpath)
    date_click.click()

    checkIn_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/input'
    date_inputs(driver, checkIn_xpath, checkin_date)

    checkOut_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/input'
    date_inputs(driver, checkOut_xpath, checkout_date)

    start_element_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[4]/div/button[2]/span'
    start_element = driver.find_element(By.XPATH, start_element_xpath)
    start_element.click()
    
    first_element_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[2]/div[2]/main/c-wiz/span/c-wiz/c-wiz[4]/div/a'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, first_element_xpath)))   
    first_element = driver.find_element(By.XPATH, first_element_xpath)
    first_element.click()

    # 탭이 포함된 상위 div 선택
    tabs_container_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[1]/div/div/c-wiz/div/div[2]/div/div[2]'
    process_accomodation_tab(driver, tabs_container_xpath)

    driver.quit()

def convert_price_to_int(price_str):
    numeric_str = price_str.replace('₩', '').replace(',', '')
    return int(numeric_str)
