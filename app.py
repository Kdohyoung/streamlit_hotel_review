import streamlit as st
from app_home import run_home
import string
import nltk

def main():
    st.title('호텔 정보제공 및 추천')
    menu = ['Home','EDA','ML']
    choice =st.sidebar.selectbox('메뉴 선택', menu)
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        pass
    elif choice == menu[2] :
        pass


if __name__ == '__main__' :
    main()
