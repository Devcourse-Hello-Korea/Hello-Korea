import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from .models import *
from .experience_constant import *

def GyeongJuCrawler(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    typename = soup.find('h3', id='pageTitle').text
    typeinfo = TypeInfo(type=typename) # 타입 설정
    typeinfo.save()

    call = []
    address = []
    homepage = []
    if typename == '전통문화체험':
        result = soup.find('div', 'exper2')
        names = result.find_all('dt')
        descriptions = result.find_all('dd')
        additional_info = result.find_all('ul')
        
        # 문화체혐명, 설명 초기화
        for i in range(len(names)):
            names[i] = names[i].text
            descriptions[i] = descriptions[i].text
            
        for info in additional_info:
            item = info.find_all('li')
            # 문의전화의 텍스트 형태가 '문의전화 000-000-0000' 형태 여서 불필요 요소 제거가 필요.
            call.append(item[0].text.replace('문의전화 ', ''))
            address.append(item[1].text.replace('주소 ', ''))
            homepage.append(item[2].text.replace('홈페이지 ', ''))
    else:
        table = soup.find_all('table')
        table_row = []
        for i in table:
            tr = i.find('tbody').find_all('tr')
            for j in tr:
                table_row.append(j)
        
        names = []
        descriptions = []
        
        if typename == '의복체험':
            for item in table_row:
                cell = item.find_all('td')
                names.append(cell[0].text)
                address.append(cell[1].text)
                descriptions.append(cell[2].text.replace('</li>', '').replace('ul', '').replace('</ul>', '').replace('<li>', '').strip())
                if len(cell[3].find_all('li')) == 0:
                    call.append(cell[3].text)
                    homepage.append('')
                else:
                    contact = cell[3].find_all('li')
                    call.append(contact[0].text)
                    homepage.append(contact[1].find('a').attrs['href'])
        else:
            for item in table_row:
                #업체명
                cell = item.find_all('td')
                names.append(cell[0].text)
                descriptions.append(cell[1].text)
                if len(cell[3].find_all('a')) == 0:
                    homepage.append('')
                else:
                    homepage.append(cell[3].find('a').attrs['href'])

                contact = cell[2].find_all('li')
                call.append(contact[0].text.replace('전화 : ', '').replace('\n', ' ').strip())
                address.append(contact[1].text.replace('주소 : ', '').replace('주소: ', '').strip())
                
    length = len(names)
    for i in range(length):
        culture_experience = TraditionExperienceInfo(
            name = names[i],
            info = descriptions[i],
            call = call[i],
            address = address[i],
            homepage = homepage[i],
            type = typeinfo,
        )
        culture_experience.save()
