from bs4 import BeautifulSoup
import time
import requests
from .models import *

user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

# 음식 데이터
def get_food_data(url, kind, page):
    for i in range(1, page+1):
        res = requests.get(url.format(i), user_agent)
        soup = BeautifulSoup(res.text, "html.parser")
        div_tags = soup.find_all("div","cont")
        for div in div_tags:
            dd_tag = div.find("dd")
            shop_name = dd_tag.find("p", "title").text

            li_tags = div.find_all("li")
            shop_address = li_tags[0].text.replace("주소", "")
            shop_number = li_tags[1].text.replace("전화번호", "")

            if kind == 'korean':
                korean_model = korean_food_model(name=shop_name, address=shop_address, number=shop_number)
                korean_model.save()
            
            elif kind == 'western':
                western_model = western_food_model(name=shop_name, address=shop_address, number=shop_number)
                western_model.save()

            elif kind == 'japanese':
                japanese_model = japanese_food_model(name=shop_name, address=shop_address, number=shop_number)
                japanese_model.save()

            elif kind == 'chinese':
                chinese_model = chinese_food_model(name=shop_name, address=shop_address, number=shop_number)
                chinese_model.save()

        time.sleep(1)




