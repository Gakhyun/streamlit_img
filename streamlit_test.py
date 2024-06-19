# steamlit 라이브러리 설치 후 시작함
# 실행하기 위해서는 새 터미널을 만들어서 아래애 streamlit run streamlit.py 해준다

import streamlit as st
from PIL import Image

# st.title("안녕하세요.")
# st.header("당각현")

st.sidebar.header("로그인")
user_id = st.sidebar.text_input("아이디 입력", value = '', max_chars=15)
user_pw = st.sidebar.text_input("비밀번호 입력", value = '', type='password')

if user_id == 'gakhyun' and user_pw == '1234':
    st.sidebar.header("그림 목록")
    sel_options = ['','진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '생명의 나무', '월하정인']
    user_opt = st.sidebar.selectbox("좋아하는 작품은?", sel_options, index=0)
    st.sidebar.write("**선택한 그림은**", user_opt)

    # 메인 화면
    st.subheader("메인 화면")

    image_files = ["Welcome.png", "Vermeer.png", "Gogh.png", "Munch.png", "Klimt.jpg", "ShinYoonbok.png"]
    sel_index = sel_options.index(user_opt)
    img_file = image_files[sel_index]
    img_local = Image.open(f'{img_file}')
    st.image(img_local, caption=user_opt)
