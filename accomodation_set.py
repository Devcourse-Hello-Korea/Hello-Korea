import sys, os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hello_Korea.settings")
django.setup()
from GyeongJu.Accomodation.accomodation_trans import trans_set
from GyeongJu.Accomodation.accomodation_crawl import crawl_set

if __name__ == '__main__':
    try:
        value = int(sys.argv[1])
        if value != 0:
            crawl_set(value)
        else:
            trans_set()
    except Exception as e:
        print(e)
