import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from .models import *

def GyeongJuCrawler():
    response = requests.get("https://www.gyeongju.go.kr/tour/page.do?mnu_uid=2318&")
    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find('div', 'exper2')

    experience_names = result.find_all('dt')
    descriptions = result.find_all('dd')
    additional_info = result.find_all('ul')

    call = []
    address = []
    homepage = []

    for info in additional_info:
        item = info.find_all('li')
        # 문의전화의 텍스트 형태가 '문의전화 000-000-0000' 형태 여서 불필요 요소 제거가 필요.
        call.append(item[0].text.replace('문의전화 ', ''))
        address.append(item[1].text.replace('주소 ', ''))
        homepage.append(item[2].text.replace('홈페이지 ', ''))
    length = len(experience_names)

    for i in range(length):
        culture_experience = TraditionExperienceInfo(
            name = experience_names[i].text,
            info = descriptions[i].text.replace('\r', '').replace('\n', '').replace('\t', ''),
            call = call[i],
            address = address[i],
            homepage = homepage[i],
        )
        culture_experience.save()
    
# 신라 문화원 크롤링
def SillaCrawler():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://silla.or.kr/")
    hover_tab = driver.find_element(By.CLASS_NAME, "menu-item-3531") # 마우스를 올려놓아야 텍스트 스크래이핑 가능
    webdriver.ActionChains(driver).move_to_element(hover_tab).perform()
    link_texts = hover_tab.find_element(By.TAG_NAME, "ul").find_elements(By.TAG_NAME, "li")

    culture_experience = {}
    length = len(link_texts)

    for i in range(length):
        name = link_texts[i].text
        culture_experience['문화체험{}'.format(i+1)] = {'체험명': name, '홈페이지': 'https://silla.or.kr/체험-행사/' + name.replace(' ', '-')}

    driver.quit()
