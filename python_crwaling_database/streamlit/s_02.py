import streamlit as st
import random
# 컴퓨터 숫자 선택
if 'c_num' not in st.session_state:
    st.session_state['c_num'] = random.randint(1,100)
c_num = st.session_state.c_num
# 숫자 입력 1~100 사이
h_num = st.number_input('숫자 입력',1,100)

if st.button('결과 확인'):    
    if c_num > h_num:        
        st.write('다운')
    elif c_num < h_num:        
        st.write('업')
    else:
        st.write('컴퓨터 숫자:',c_num)
        st.write('정답')
        st.balloons()  # 축하 애니메이션
