from googletrans import Translator
from .accomodation_models import AccomodationInfo, AccomodationForm_model

languages = ['en', 'ja', 'zh-cn', 'zh-tw', 'de', 'ru']

def translate_all_data(selected_month):
    data = AccomodationInfo.objects.filter(lang='ko', month=selected_month)
    for lang in languages:
        t_data = translate_data(data, lang)
        for item in t_data:
            item.save()

def translate_data(data, lang):
    translator = Translator()
    translated_data = []
    for item in data:
        translated_item = AccomodationInfo(
            lang=lang,
            location=translator.translate(item.location, src='ko', dest=lang).text,
            name=translator.translate(item.name, src='ko', dest=lang).text,
            month=item.month,
            link=item.link,
            img_src1=item.img_src1,
            img_src2=item.img_src2,
            img_src3=item.img_src3
        )
        translated_data.append(translated_item)
    return translated_data


def set_accomodation_form():
    translator = Translator()
    AccomodationForm_model.objects.all().delete()
    accomodation_form = AccomodationForm_model(
        lang='ko', 
        no_results_text='결과가 없습니다.',
        link_text='링크',
        crawl_button_text='크롤링',
        search_button_text='검색',
        page_title='숙소 정보',
    )
    accomodation_form.save()

    for lang in languages:
        translated_no_results_text = translator.translate(accomodation_form.no_results_text, src='ko', dest=lang).text
        translated_link_text = translator.translate(accomodation_form.link_text, src='ko', dest=lang).text
        translated_crawl_button_text = translator.translate(accomodation_form.crawl_button_text, src='ko', dest=lang).text
        translated_search_button_text = translator.translate(accomodation_form.search_button_text, src='ko', dest=lang).text
        translated_page_title = translator.translate(accomodation_form.page_title, src='ko', dest=lang).text

        translated_form = AccomodationForm_model(
            lang=lang,
            no_results_text=translated_no_results_text,
            link_text=translated_link_text,
            crawl_button_text=translated_crawl_button_text,
            search_button_text=translated_search_button_text,
            page_title=translated_page_title,
        )
        translated_form.save()

        
def trans_set():
    set_accomodation_form()
