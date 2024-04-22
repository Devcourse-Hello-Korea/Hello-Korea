from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .accomodation_models import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from datetime import datetime, timedelta
from .accomodation_trans import translate_all_data
from django.db import IntegrityError

def date_inputs(driver, path, date):
    date_input = driver.find_element(By.XPATH, path)
    date_input.click()
    date_input.send_keys(Keys.CONTROL, 'a')
    date_input.send_keys(Keys.BACK_SPACE)
    date_input.send_keys(date)
    date_input.send_keys(Keys.ENTER)

def process_accomodation_tab(driver, tabs_container_xpath, checkin_date):
    wait = WebDriverWait(driver, 10)
    tabs_container = wait.until(EC.presence_of_element_located((By.XPATH, tabs_container_xpath)))
    tabs = tabs_container.find_elements(By.XPATH, './div')
    num_of_tabs = len(tabs)

    month_str = checkin_date.split("월")[0]
    accomodation_month = month_str
    AccomodationInfo.objects.filter(month=accomodation_month).delete()
    #for i in range(4, num_of_tabs + 4):
    plus = 4
    for i in range(4, 5 + plus):
        # 탭 클릭
        tab_xpath = f'{tabs_container_xpath}/div[{i}]'
        wait = WebDriverWait(driver, 10)
        tab = wait.until(EC.visibility_of_element_located((By.XPATH, tab_xpath)))
        driver.execute_script("arguments[0].click();", tab)

        try:
            accomodation_name = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[1]/div[1]/c-wiz/div/h1'))).text
        except NoSuchElementException:
            accomodation_name = "이름 없음"  # 호텔 이름이 없는 경우
        except StaleElementReferenceException:
            accomodation_name = "이름 없음"

        try:
            accomodation_location = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[1]/div/section/div[1]/div[1]/div/div[2]/span').text
        except NoSuchElementException:
            accomodation_location = "장소 없음"
        except StaleElementReferenceException:
            accomodation_location = "장소 없음"  # 호텔 위치가 없는 경우
        
        img_xpaths = [
            '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[2]/div/div/div/div[1]/div[1]/div/div/div[1]/img',
            '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[2]/div/div/div/div[1]/div[1]/div/div/div[2]/img',
            '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[2]/div/div/div/div[1]/div[1]/div/div/div[3]/img'
        ]
        accomodation_img_srcs = []
        for xpath in img_xpaths:
            try:
                accomodation_img = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
                accomodation_img_srcs.append(accomodation_img.get_attribute('src'))
            except NoSuchElementException:
                # 이미지를 찾을 수 없는 경우, 리스트에 빈 문자열 추가
                accomodation_img_srcs.append("")
        
        try:
            accomodation_link_href = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[1]/div/section/div[3]/span[1]/div/a')
            accomodation_link = accomodation_link_href.get_attribute('href')
        except NoSuchElementException:
            try:
                accomodation_link_href = driver.find_element(By.XPATH, '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div[2]/span[1]/c-wiz[1]/c-wiz[1]/div/section/div[2]/span[1]/div/a')
                accomodation_link = accomodation_link_href.get_attribute('href')
            except NoSuchElementException:
                accomodation_link = ""
        # Django 모델에 저장
        try:
            accomodation_info = AccomodationInfo(lang = 'ko',
                                                location=accomodation_location, name=accomodation_name, 
                                                month=accomodation_month, link = accomodation_link,
                                                img_src1 = accomodation_img_srcs[0],
                                                img_src2 = accomodation_img_srcs[1],
                                                img_src3 = accomodation_img_srcs[2],
                                                )
            accomodation_info.save()
        except IntegrityError:
            plus += 1
            continue

def set_dates_and_crawl(selected_month):
    url = "https://www.google.com/travel/search?q=%EA%B2%BD%EC%A3%BC%20%EC%88%99%EC%86%8C&g2lb=2503771%2C2503781%2C4284970%2C4291517%2C4814050%2C4874190%2C4893075%2C4965990%2C72277293%2C72302247%2C72317059%2C72406588%2C72414906%2C72421566%2C72458066%2C72462234%2C72470440%2C72470899%2C72471280%2C72472051%2C72473841%2C72481458%2C72485656%2C72485658%2C72486593%2C72494250%2C72513422%2C72513513%2C72523972%2C72530239%2C72534000%2C72536387%2C72538597%2C72549171%2C72549174%2C72561417%2C72561423&hl=ko-KR&gl=kr&ssta=1&ts=CAESCgoCCAMKAggDEAAaHhIcEhQKBwjoDxAEGA8SBwjoDxAEGBAYATIECAAQACoHCgU6A0tSVw&qs=CAAgACgA&ap=KigKEglWdogmq6tBQBF8kGVhiiRgQBISCXPseYl8GUJAEXyQZSH_OmBAMABoAQ&ictx=111&ved=0CAAQ5JsGahcKEwjAxZq6k7-FAxUAAAAAHQAAAAAQdw"
    if int(selected_month) == datetime.today().month:
        checkin_date = datetime.today() + timedelta(days=1)
        checkout_date = checkin_date + timedelta(days=1)
        checkin_date = "{}월 {}".format(checkin_date.month, checkin_date.day)
        checkout_date = "{}월 {}".format(checkout_date.month, checkout_date.day)
    else:
        checkin_date = "{}월 15".format(selected_month)
        checkout_date = "{}월 16".format(selected_month)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get(url)
    driver.execute_script("window.focus();")

    date_click_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/input'
    date_click = driver.find_element(By.XPATH, date_click_xpath)
    date_click.click()

    checkIn_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/input'
    date_inputs(driver, checkIn_xpath, checkin_date)

    checkOut_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/input'
    date_inputs(driver, checkOut_xpath, checkout_date)

    start_element_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[1]/c-wiz/div/div/div[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/div[4]/div/button[2]/span'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, start_element_xpath)))
    start_element = driver.find_element(By.XPATH, start_element_xpath)
    start_element.click()
    try:
        first_element_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[1]/div[2]/div[2]/main/c-wiz/span/c-wiz/c-wiz[5]/div/a'
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, first_element_xpath)))   
        first_element = driver.find_element(By.XPATH, first_element_xpath)
        first_element.click()
    except StaleElementReferenceException:
        set_dates_and_crawl(selected_month)
        driver.quit()

    # 탭이 포함된 상위 div 선택
    tabs_container_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[1]/div/div/c-wiz/div/div[2]/div/div[2]'
    process_accomodation_tab(driver, tabs_container_xpath, checkin_date)

    driver.quit()

def data_delete(selected_month):
    existing_data = AccomodationInfo.objects.filter(month=selected_month)
    if existing_data.exists():
        existing_data.delete()


def crawl_set(selected_month):
    data_delete(selected_month)
    set_dates_and_crawl(selected_month)
    translate_all_data(selected_month)
