import streamlit as st
from PIL import Image

def run_home() :
    st.subheader('호텔의 정보를 제공하고 당신이 가본 호텔과 유사한 호텔을 추천 해드립니다.')
    url = 'https://mblogthumb-phinf.pstatic.net/20160822_280/the_trip_1471844884310AySd7_JPEG/%B6%F3%BD%BA%BA%A3%B0%A1%BD%BA.jpg?type=w800'
    st.image(url)

    url1 = 'https://kilta.funandzam.com/wp-content/uploads/2021/08/wafaf.png'
    st.image(url1)
