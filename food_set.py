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
    text_food_form.objects.all().delete()
    get_food_data(KOREAN_URL, 'korean', 1)#11
    get_food_data(WESTERN_URL, 'western', 1)#4
    get_food_data(JAPANESE_URL, 'japanese',1)#2
    get_food_data(CHINESE_URL, 'chinese',1)
    food_form = text_food_form(
        lang='ko', 
        korean_text='한국 음식',
        western_text='서양 음식',
        japanese_text='일본 음식',
        chinese_text='중국 음식',
    )
    food_form.save()

languages = ['en', 'ja', 'zh-cn', 'zh-tw', 'de', 'ru'] #'ko'

def translate_all_data_food():
    translator = Translator()
    korean_data = korean_food_model.objects.filter(lang='ko')
    western_data = western_food_model.objects.filter(lang='ko')
    japanese_data = japanese_food_model.objects.filter(lang='ko')
    chinese_data = chinese_food_model.objects.filter(lang='ko')
    food_form = text_food_form.objects.filter(lang='ko').first()
    for lang in languages:
        time.sleep(random.random())
        new_data = text_food_form(
            lang=lang, 
            korean_text=translator.translate(food_form.korean_text, src='ko', dest=lang).text,
            western_text=translator.translate(food_form.western_text, src='ko', dest=lang).text,
            japanese_text=translator.translate(food_form.japanese_text, src='ko', dest=lang).text,
            chinese_text=translator.translate(food_form.chinese_text, src='ko', dest=lang).text,
        )
        new_data.save()
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
