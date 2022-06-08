# streamlit_hotel_review
=============
###### 호텔 데이터 분석 및 추천 시스템입니다

호텔 데이터와 평점, 지역을 이용하여 고객들의 호텔 만족도를 조사하여 유사한 호텔을 추천합니다.
사용한 언어는 python 이며 Google Colab 을 이용하여 코딩하고 인공지능을 학습 시켰습니다.
데이터를 시각화하기위해 Visual Studio Code 로 작업한 데이터를 streamlit에 적용 시켰습니다.


데이터 출처 : https://www.kaggle.com/datasets/datafiniti/hotel-reviews

데이터의 컬럼 설명
=============

1. address  :  주소
2. categories : 호텔,모텔
3. city : EX) 도시
4. country : 나라
5. latitude : 경도
6. longitude : 위도 
7. name : 호텔 이름
8. province : 지역 
9. dateUpdated : 리뷰 업데이트 시간
10. reviews.rating  : 별점
11. reviews.text : 호텔 리뷰
12. reviews.username  : 리뷰를 쓴 유저의 이름


사용한 라이브러리 
=============

1.import streamlit as st

2.from streamlit_option_menu import option_menu

3.import pandas as pd

4.from PIL import Image

5.import numpy as np

6.import seaborn as sb

호텔추천 시스템 
============
데이터를 피봇 테이블하여
전체 데이터와의 상관 관계를 구한후 
상관 관계과 높은순으로 추천
