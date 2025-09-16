# pip install streamlit  - 터미널에서 실행
import streamlit as st
st.title('타이틀')
st.header("헤더")
st.subheader('서브헤더')
st.button('버튼')
st.checkbox('체크박스')
st.radio('레디오박스',('a','b','c'))
st.selectbox('셀렉트 박스',(1,2,3,4,5,6,7,8,9,10))
st.slider('슬라이더',0,100,50)  # 최대 최소 기본값
st.text_input('텍스트 상자')