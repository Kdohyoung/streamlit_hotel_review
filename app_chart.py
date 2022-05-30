import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb
from PIL import Image


def run_chart() :
    df=pd.read_csv('data/hotels.csv',index_col=0)
    st.subheader('별점의 데이터 갯수')
    st.text('내림차순')
    fig = plt.figure()
    my_order = df['reviews.rating'].value_counts().index
    sb.countplot(data=df, x= 'reviews.rating' ,  order=my_order)
    st.pyplot(fig)
    
    st.subheader('별점 평균의 히스토그램')

    fig2 = plt.figure()
    df_mean = df.groupby('name')['reviews.rating'].mean()
    df_mean = df_mean.to_frame()
    df_mean.columns=['ratings_mean']
    df_size = df.groupby('name').size()
    df_size = df_size.to_frame()
    df_size.columns=['count']
    df_mc = df_mean.join(df_size)
    df_mc['ratings_mean'].hist()
    st.pyplot(fig2)

    st.subheader('리뷰 갯수의 히스토그램')

    fig3 = plt.figure()
    df_mc['count'].hist()
    st.pyplot(fig3)
