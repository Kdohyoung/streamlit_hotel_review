import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sb
from PIL import Image





def run_ml() :
    df=pd.read_csv('data/hotels.csv',index_col=0)
    st.subheader('당신이 선택한 호텔과 유사한 호텔 추천')
    df2=df.pivot_table(values='reviews.rating',index='reviews.username',columns='name',aggfunc='mean')
    all_corr = df2.corr(min_periods=5)
    hotels = df['name'].unique()
    hotels_name = st.selectbox('호텔선택',hotels)
    all_corr[hotels]
    recom_hotels=all_corr[hotels_name].dropna()
    recom_hotels.columns=['correlation']
    recom_hotels = recom_hotels.sort_values(ascending=False).to_frame()
    st.dataframe(recom_hotels)
