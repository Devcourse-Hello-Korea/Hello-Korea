from googletrans import Translator
from .souvenir_models import *

languages = ['en', 'ja', 'zh-cn', 'zh-tw', 'de', 'ru']

def translate_all_souvenir():
    translator = Translator()
    breads = Bread.objects.filter(lang='ko')
    shops = Shop.objects.filter(lang='ko')
    souvenir_form = text_souvenir_form(
        lang='ko', 
        shop='기념품 가게',
        bread='경주의 빵'
    )
    souvenir_form.save()
    for lang in languages:
        new_data = text_souvenir_form(
            lang=lang, 
            shop=translator.translate(souvenir_form.shop, src='ko', dest=lang).text,
            bread=translator.translate(souvenir_form.bread, src='ko', dest=lang).text,
        )
        new_data.save()
        for data in breads:
            new_data = Bread(
                lang=lang,
                name=translator.translate(data.name, src='ko', dest=lang).text,
                image = data.image,
                description=translator.translate(data.description, src='ko', dest=lang).text
            )
            new_data.save()
        for data in shops:
            new_data = Shop(
                lang=lang,
                name=translator.translate(data.name, src='ko', dest=lang).text,
                image = data.image,
                address=translator.translate(data.address, src='ko', dest=lang).text,
                business_hours = translator.translate(data.business_hours, src='ko', dest=lang).text
            )
            new_data.save()
