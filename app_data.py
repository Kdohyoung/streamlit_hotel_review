import streamlit as st
import pandas as pd
from PIL import Image

def run_data() :
    st.subheader('호텔 전체 데이터 입니다.')
    df=pd.read_csv('data/hotels.csv',index_col=0)
    st.dataframe(df)

    url3 = 'https://img.ev.mu/images/villes/8277/600x400/8277.jpg'
    st.image(url3)
    st.text('Hotel Russo Palace')

    st.subheader('호텔 데이터')
    sentence = st.text_input('호텔이름 입력')
    if st.button('검색'):
        ht_info = df.loc[df['name']== sentence]
        st.write(ht_info)
        
        




    st.subheader('리뷰가 가장 많은 호텔 top5')
    re_df = df.groupby('name')['reviews.text'].count().to_frame()
    re_df1 = re_df.sort_values('reviews.text',ascending=False)
    st.dataframe(re_df1.head(5))

    url5 = 'https://cdn0.weddingwire.com/vendor/648759/3_2/960/jpg/1484065354813-alex7.jpeg'
    st.image(url5)
    st.text('hotel - The Alexandrian, Autograph Collection')

    st.subheader('bset 호텔 top5')
    st.text('data = 리뷰수 50개 이상인 호텔')
    df_mean = df.groupby('name')['reviews.rating'].mean()
    df_mean = df_mean.to_frame()
    df_mean.columns=['ratings_mean']
    df_size = df.groupby('name').size()
    df_size = df_size.to_frame()
    df_size.columns=['count']
    df_mc = df_mean.join(df_size)
    df_mc = df_mc.loc[df_mc['count'] > 50, ].sort_values('ratings_mean',ascending=False).round(1)
    st.dataframe(df_mc['ratings_mean'].head(5))

    url4 = 'https://exp.cdn-hotels.com/hotels/2000000/1130000/1120500/1120449/f0b249fa_z.jpg?impolicy=fcrop&w=773&h=530&q=high'
    st.image(url4)
    st.text('hotel - Excellence Riviera Cancun - Adults Only - All Inclusive')

    st.subheader('worst 호텔 top5')
    st.text('data = 리뷰수 50개 이상인 호텔')
    st.dataframe(df_mc['ratings_mean'].tail(5))


    st.subheader('가장 많은 리뷰를 쓴 여행객 top5')
    visiter  = df['reviews.username'].value_counts().to_frame()
    visiter_count = visiter.iloc[2:7,:]
    st.dataframe(visiter_count)

    
    st.subheader('여행객 리뷰 데이터')
    visit_name = st.text_input('여행객 이름 입력')
    if st.button('find'):
        visiter_info = df.loc[df['reviews.username']== visit_name]
        st.write(visiter_info)
