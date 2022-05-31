import streamlit as st
from app_home import run_home
from app_data import run_data
from app_ldata import run_ldata
from app_chart import run_chart
from app_ml import run_ml



def main():
    st.title('호텔 정보제공 및 추천')
    menu = ['Home','호텔별 리뷰 평점 데이터','지역별 호텔 데이터','차트','추천']
    choice =st.sidebar.selectbox('메뉴 선택', menu)
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_data()
    elif choice == menu[2] :
        run_ldata()
    elif choice == menu[3] :
        run_chart()
    elif choice == menu[4] :
        run_ml()



if __name__ == '__main__' :
    main()
