import os
import django
import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hello_Korea.settings")
django.setup()

from GyeongJu.Souvenir.souvenir_models import Breads

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
    
if __name__=='__main__':
    breads = BreadInfo()
    for bread in breads:
        bread_instance = Breads.objects.create(
            name=bread['name'],
            image=bread['image_url'],
            description=bread['description'],
        )