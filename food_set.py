import os, django
from googletrans import Translator
import time, random


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hello_Korea.settings")
django.setup()

from GyeongJu.food.food_models import *
from GyeongJu.food.food_data import *
from GyeongJu.food.food_contants import *

def food_data_set():
    korean_food_model.objects.all().delete()
    western_food_model.objects.all().delete()
    japanese_food_model.objects.all().delete()
    chinese_food_model.objects.all().delete()
    get_food_data(KOREAN_URL, 'korean', 1)#11
    get_food_data(WESTERN_URL, 'western', 1)#4
    get_food_data(JAPANESE_URL, 'japanese',1)#2
    get_food_data(CHINESE_URL, 'chinese',1)

languages = ['en', 'ja', 'zh-cn', 'zh-tw', 'de', 'ru'] #'ko'

def translate_all_data_food():
    translator = Translator()
    korean_data = korean_food_model.objects.filter(lang='ko')
    western_data = western_food_model.objects.filter(lang='ko')
    japanese_data = japanese_food_model.objects.filter(lang='ko')
    chinese_data = chinese_food_model.objects.filter(lang='ko')
    for lang in languages:
        time.sleep(random.random())
        for data in korean_data:
            time.sleep(0.3)
            new_data = korean_food_model(
                lang = lang,
                name = translator.translate(data.name, src='ko', dest=lang).text,
                address = translator.translate(data.address, src='ko', dest=lang).text,
                number = data.number
            )
            new_data.save()
        for data in western_data:
            time.sleep(0.3)
            new_data = western_food_model(
                lang = lang,
                name = translator.translate(data.name, src='ko', dest=lang).text,
                address = translator.translate(data.address, src='ko', dest=lang).text,
                number = data.number
            )
            new_data.save()
        for data in japanese_data:
            time.sleep(0.3)
            new_data = japanese_food_model(
                lang = lang,
                name = translator.translate(data.name, src='ko', dest=lang).text,
                address = translator.translate(data.address, src='ko', dest=lang).text,
                number = data.number
            )
            new_data.save()
        for data in chinese_data:
            time.sleep(0.3)
            new_data = chinese_food_model(
                lang = lang,
                name = translator.translate(data.name, src='ko', dest=lang).text,
                address = translator.translate(data.address, src='ko', dest=lang).text,
                number = data.number
            )
            new_data.save()

if __name__ == '__main__':
    try:
        food_data_set()
        translate_all_data_food()
    except Exception as e:
        print(e)
