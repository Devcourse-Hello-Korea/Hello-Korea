# Hello Korea

### 1. 프로젝트 소개
‘<b>외국 관광객 유치 활성화를 위한 대한민국 여행 웹 서비스: Hello Korea</b>’는 외국인 관광객들에게 잘 알려지지 않은 한국의 숨겨진 아름다운 도시들을 소개하고 도시의 여행 정보를 한눈에 보기 쉽게 만든 웹서비스입니다. 도시의 정보를 수집하기 위해 다양한 웹사이트를 <b>크롤링</b>하여 숙소, 음식, 문화체험, 기념품 정보를 <b>시각화</b>하여 제공합니다. 또한, 영어, 중국어, 일본어를 포함한 총 7가지 언어로 모든 페이지가 <b>번역</b> 가능하므로 다양한 나라의 관광객이 간편하게 접근할 수 있습니다. 

<br>

---------------------

### 2. 프로젝트 주제 선정 이유
K-pop과 K콘텐츠의 인기로 한국에 대한 관심이 전 세계적으로 높아지고 있는 상황에서 이미 잘 알려진 지역이 아니라 한국의 다채로운 매력을 경험할 수 있도록 다양한 도시들을 소개하고 각 <b>지역의 고유한 문화와 아름다움</b>을 경험할 수 있는 기회를 제공하고자 합니다. 한국관광공사의 통계에 따르면 작년 한 해 매달 외국인 방문객 수가 꾸준하게 증가했으며, 그중 약 67%는 수도권 지역을 방문했습니다. 그러나 그 이외의 지역들은 약 2% 대에 머물렀습니다. 이러한 통계를 바탕으로 해당 지역에 대한 <b>낮은 정보 접근성을 해결하여 외국인 관광 활성화</b>를 위해  한국의 숨겨진 도시 여행 정보 제공을 프로젝트의 주제로 선정하게 됐습니다. 

<br>

---------------------

### 3. 기술 스택
<img src="https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white"> <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">


<br>

---------------------

### 4. 기대효과

1. 언어 장벽 해소 :  다국어 번역 기능을 통해 수도권 외 지역을 여행하고자 하는 외국인들이 정보를 편하게 습득할 수 있습니다.

2. 문화 교류 증진 : 서비스를 통해 외국인 관광객들이 해당 지역의 역사와 문화를 깊이 있게 이해할 수 있게 되어 한국과 외국 간의 문화 교류가 활성화되는 것을 기대할 수 있습니다

3. 경제적 효과 : 외국인 관광객의 유치 증대로 인한 해당 지역 경제 활성화, 일자리 창출 등의 경제적 효과를 기대할 수 있습니다.

4. 국제적 인지도 상승 : 서비스를 통해 해당 지역의 매력을 전세계에 알림으로써, 지역의 국제적 인지도와 브랜드 가치가 향상될 수 있습니다

<br>

-----------------------------------

### 5. 팀원

|이름|역할|GitHub|
|------|---|---|
|문소정| 작성 예정 |https://github.com/Elisha0510|
|안중현|작성 예정|https://github.com/ImJoongHyeon|
|유준상|작성 예정|https://github.com/Pikiss-personal|
|주경연|작성 예정|https://github.com/Kyoung-yeon99|


---------------------

### 6. 구동 방법

1. 필요한 라이브러리 pip install
(beautifulsoup4==4.12.3, Django==5.0.4, googletrans==4.0.0rc1, requests==2.31.0, selenium==4.19.0, webdriver-manager==4.0.1)

2. 페이지 텍스트 설정
(python accomodation_set.py 0, python hard_coded_set.py)

3. 필요한 데이터 크롤링
(python accomodation_set.py n,  python food_set.py, python souvenir_crawl.py, python tradition_crawler.py)
*(n은 현재 달부터 +10달까지의 숫자입니다. 4월이면 2~12)

4. 페이지 작동
(python manage.py runserver)

<br>

-----------------------------------
