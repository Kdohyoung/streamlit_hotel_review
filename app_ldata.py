import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_ldata() :
    st.subheader('지역별 호텔 데이터 입니다.')
    df=pd.read_csv('data/hotels.csv',index_col=0)
    city = df['city'].unique()
    city_list = st.selectbox('도시 선택',city)
    city_info = df.loc[df['city'] == city_list]
    st.dataframe(city_info)
    url7 = 'https://thumb.wishbeen.com/tYCj1LI4KtGDM6PKvHcUcN3bycs=/898x420/smart/filters:no_upscale()/wishbeen-seoul.s3.ap-northeast-2.amazonaws.com/spot/1387823748602_timessq.jpg'
    st.image(url7)
    st.text('city - new york')

    st.subheader('각 도시 호텔 별점평균   top5')
    st.text('data = 리뷰수 50개 이상인 호텔')
    city_rating = df.groupby('city')['reviews.rating'].mean().to_frame()
    city_rating =city_rating.sort_values('reviews.rating',ascending=False)
    city_size = df.groupby('city').size()
    df_size = df.groupby('name').size()
    city_size = city_size.to_frame()
    city_size.columns=['count']
    city_mc = city_rating.join(city_size)
    city_mc = city_mc.loc[city_mc['count'] > 50, ].sort_values('reviews.rating',ascending=False).round(1)
    st.dataframe(city_mc['reviews.rating'].head(5))
    
    url6 = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20130408_28%2Fdaitouryou_1365348619067gp5jh_JPEG%2FP8177861.jpg&type=sc960_832'
    st.image(url6)
    st.text('city - staten lsland')


    st.subheader('각 도시 호텔 별점평균   worst5')
    st.text('data = 리뷰수 50개 이상인 호텔')
    city_rating = df.groupby('city')['reviews.rating'].mean().to_frame()
    city_rating =city_rating.sort_values('reviews.rating',ascending=False)
    city_size = df.groupby('city').size()
    df_size = df.groupby('name').size()
    city_size = city_size.to_frame()
    city_size.columns=['count']
    city_mc = city_rating.join(city_size)
    city_mc = city_mc.loc[city_mc['count'] > 50, ].sort_values('reviews.rating',ascending=False).round(1)
    st.dataframe(city_mc['reviews.rating'].tail(5))

    st.subheader('호텔별 위도 경도 데이터.')
    df_km=df[['name','address','city','latitude','longitude']]
    df_km = df_km.drop_duplicates(['name'],keep='first')
    locaton = df['name'].unique()
    lc_list = st.selectbox('호텔선택',locaton)
    lc_info = df_km.loc[df_km['name'] == lc_list]
    st.dataframe(lc_info)
