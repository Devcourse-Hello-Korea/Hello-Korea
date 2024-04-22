import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hello_Korea.settings")
django.setup()
from GyeongJu.models import hard_coded_text
from googletrans import Translator
import time, random

languages = ['en', 'ja', 'zh-cn', 'zh-tw', 'de', 'ru'] #'ko'

def hard_coded_set():
    hard_coded_text.objects.all().delete()
    text_form = hard_coded_text(
        lang = 'ko',
        Gyeongju_text = '경주',
        Suncheon_text = '순천',
        Jeonju_text = '전주',
        lodging_text = '숙소',
        Food_text = '음식',
        Experience_text = '전통문화 체험',
        Souvenir_text = '기념품',
        Main_Gyeongju_text1 = 'K-POP이 전세계에 유명해지면서 한국에 대한 관심도가 올라가고 있습니다. 그러나 관광객은 그만큼 증가하지는 않았습니다.',
        Main_Gyeongju_text2 = '때문에 외국인 관광객들에게 잘 알려지지 않은 한국의 숨겨진 아름다운 도시들을 소개하고 도시의 여행 정보를 한눈에 보기 쉽게 만들어 한국 여행지의 매력을 알리려는 웹서비스입니다.',
        Main_Gyeongju_text3 = '도시의 정보를 수집하기 위해 다양한 웹사이트를 크롤링하여 숙소, 음식, 문화체험, 기념품 정보를 시각화하여 제공합니다.',
        Main_Gyeongju_text4 = '또한, 영어, 중국어, 일본어를 포함한 총 7가지 언어로 모든 페이지가 번역 가능하므로 다양한 나라의 관광객이 간편하게 접근할 수 있습니다.',
    )
    text_form.save()
    translator = Translator()
    for lang in languages:
        time.sleep(random.random())
        new_data = hard_coded_text(
            lang=lang, 
            Gyeongju_text=translator.translate(text_form.Gyeongju_text, src='ko', dest=lang).text,
            Suncheon_text=translator.translate(text_form.Suncheon_text, src='ko', dest=lang).text,
            Jeonju_text=translator.translate(text_form.Jeonju_text, src='ko', dest=lang).text,
            lodging_text=translator.translate(text_form.lodging_text, src='ko', dest=lang).text,
            Food_text=translator.translate(text_form.Food_text, src='ko', dest=lang).text,
            Experience_text=translator.translate(text_form.Experience_text, src='ko', dest=lang).text,
            Souvenir_text=translator.translate(text_form.Souvenir_text, src='ko', dest=lang).text,
            Main_Gyeongju_text1=translator.translate(text_form.Main_Gyeongju_text1, src='ko', dest=lang).text,
            Main_Gyeongju_text2=translator.translate(text_form.Main_Gyeongju_text2, src='ko', dest=lang).text,
            Main_Gyeongju_text3=translator.translate(text_form.Main_Gyeongju_text3, src='ko', dest=lang).text,
            Main_Gyeongju_text4=translator.translate(text_form.Main_Gyeongju_text4, src='ko', dest=lang).text,
        )
        new_data.save()

if __name__ == '__main__':
    try:
        hard_coded_set()
    except Exception as e:
        print(e)
