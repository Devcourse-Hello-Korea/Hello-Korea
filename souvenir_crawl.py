import os
import django
import requests
from bs4 import BeautifulSoup
from django.db import transaction
#from geopy.geocoders import Nominatim
#geo_local = Nominatim(user_agent='South Korea')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hello_Korea.settings")
django.setup()

from GyeongJu.Souvenir.souvenir_models import Bread, Shop, ShopLocation

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
        address = ul.find_all('li')[0] #.text.split(' ')[1:]
        if address.find('ul'):  # 주소가 여러 개 있는 경우
            address = address.find('ul').find_all('li')[0].text.split(' ')[2:5]
            business_hours = ['평일', '10시~19시', '주말', '10시~20시']
        else:
            address = address.text.split(' ')[1:]
            business_hours = ul.find_all('li')[1].text.split(' ')[1:]
            if business_hours[1] == '(휴무가':
                business_hours[1], business_hours[2], business_hours[3] = '(참고','휴무','비정기적)'

        # 기념품 가게 정보를 딕셔너리로 저장
        shop = {
            "name": name,
            "image_url": image_url,
            "address": ' '.join(address),
            "business_hours": ' '.join(business_hours)
        }
        shops.append(shop)
    
    return shops

"""
def GeoCoding(shops):
    locations = []
    for shop in shops:
        try:
            geo = geo_local.geocode(shop['address'])
            x, y = geo.latitude, geo.longtitude
            locations.append((x, y))
            print(shop, shop['address'], x, y)
        except:
            locations.append((0, 0))
    
    return locations 
"""

if __name__=='__main__':
    Bread.objects.all().delete()
    Shop.objects.all().delete()
    ShopLocation.objects.all().delete()
    
    breads = BreadInfo()
    shops = ShopInfo()
    locations = [
        [35.8405942, 129.2134083], 
        [35.8358405, 129.2125724],
        [35.8365075, 129.2083913],
        [35.8376421, 129.2085434],
        [35.8387433, 129.2097404],
        [35.8387058, 129.2061467],
        [35.8414477, 129.2123418],
        ]
    
    for bread in breads:
        bread_instance = Bread.objects.create(
            name=bread['name'],
            image=bread['image_url'],
            description=bread['description'],
        )

    with transaction.atomic():
        for shop, location in zip(shops, locations):
            shop_instace = Shop.objects.create(
                name=shop['name'],
                image=shop['image_url'],
                address=shop['address'],
                business_hours=shop['business_hours'],
            )
        
            location_instance = ShopLocation.objects.create(
                shop = shop_instace,
                lat = location[0],
                lng = location[1],
            )
