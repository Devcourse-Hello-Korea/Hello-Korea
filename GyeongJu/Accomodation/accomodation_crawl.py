from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .accomodation_models import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from datetime import datetime, timedelta

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
    #for i in range(1, num_of_tabs + 1):
    for i in range(4, 5 + 4):
    #for i in range(1, 4):
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
        accomodation_info = AccomodationInfo(location=accomodation_location, name=accomodation_name, 
                                             month=accomodation_month, link = accomodation_link,
                                             img_src1 = accomodation_img_srcs[0],
                                             img_src2 = accomodation_img_srcs[1],
                                             img_src3 = accomodation_img_srcs[2],
                                             )
        accomodation_info.save()

def set_dates_and_crawl(url, checkin_date, checkout_date):
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
        change_date1 = datetime.strptime(f"{checkin_date}", "%m월 %d")
        change_date2 = datetime.strptime(f"{checkout_date}", "%m월 %d")
        checkin_date2 = change_date1 + timedelta(days=1)
        checkout_date2 = change_date2 + timedelta(days=1)
        checkin_date_str2 = "{}월 {}".format(checkin_date2.month, checkin_date2.day)
        checkout_date_str2 = "{}월 {}".format(checkout_date2.month, checkout_date2.day)
        set_dates_and_crawl(url, checkin_date_str2, checkout_date_str2)
        driver.quit()

    # 탭이 포함된 상위 div 선택
    tabs_container_xpath = '/html/body/c-wiz[2]/div/c-wiz/div[1]/div[2]/div[1]/div/div/c-wiz/div/div[2]/div/div[2]'
    process_accomodation_tab(driver, tabs_container_xpath, checkin_date)

    driver.quit()