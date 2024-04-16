import os
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hello_Korea.settings")
django.setup()

from GyeongJu.Souvenir.souvenir_models import Bread, Shop

def BreadInfo():
    url = "https://www.gyeongju.go.kr/tour/page.do?mnu_uid=2342&"  # 경주빵
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    breads = []

    for li in soup.select("div.specList ul li"):
        # 이미지 URL 추출
        image_url = "https://www.gyeongju.go.kr/"+li.img["src"]
        # 빵 이름 추출
        name = li.p.span.text
        # 빵 설명 추출
        info = soup.select_one(li.a['href'])
        description = info.find('p').text
        # 빵 정보를 딕셔너리로 저장
        bread = {
            "name": name,
            "image_url": image_url,
            "description": description
        }
        breads.append(bread)

    return breads


def ShopInfo():
    url = "https://www.gyeongju.go.kr/tour/page.do?mnu_uid=2706&"  # 기념품 가게 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    shops = []

    divs = soup.find('div', class_='exper2 town')
    for div in divs.find_all('div'):
        # 기념품 가게 이름 추출
        name = div.find('dt').text.strip()
        # 이미지 URL 추출
        image_url = "https://www.gyeongju.go.kr/"+div.img["src"]
        
        ul = div.find('ul')  # Find the <ul> element within the <div>
        # Extract data from the first and second <li> elements
        address = ul.find_all('li')[0].text.split(' ')[1:]
        business_hours = ul.find_all('li')[1].text.split(' ')[1:]

        # 기념품 가게 정보를 딕셔너리로 저장
        shop = {
            "name": name,
            "image_url": image_url,
            "address": ' '.join(address),
            "business_hours": ' '.join(business_hours)
        }
        shops.append(shop)
    
    return shops

    
if __name__=='__main__':
    breads = BreadInfo()
    for bread in breads:
        bread_instance = Bread.objects.create(
            name=bread['name'],
            image=bread['image_url'],
            description=bread['description'],
        )
    shops = ShopInfo()
    for shop in shops:
        shop_instace = Shop.objects.create(
            name=shop['name'],
            image=shop['image_url'],
            address=shop['address'],
            business_hours=shop['business_hours'],
        )