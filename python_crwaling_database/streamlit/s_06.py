import streamlit as st
import random
from streamlit_autorefresh import st_autorefresh


# 페이지 기본 설정
st.set_page_config(
    page_title="Streamlit 레이아웃 예제",
    page_icon=":heart_eyes:",
    layout="wide"  # 전체 페이지를 wide 모드로 설정
)

# 사이드바 메뉴 생성
with st.sidebar:
    st.title("게임")
    selected_menu = st.radio(
        "원하시는 게임을 선택하세요:",
        ["숫자맞추기", "가위바위보"]
    )

# 메인 컨텐츠 영역
import random
def show_game1():
    st.header("숫자맞추기")
    st.write("환영합니다! 이곳은 숫자맞추기 게임 페이지입니다.")

    if 'c_number' not in st.session_state:
        st.session_state.c_number = random.randint(1, 100)    
    c_num = st.session_state.c_number

    st.number_input("1에서 100 사이의 숫자를 입력하세요:", 0, 100, key='h_number')
    h_number = st.session_state.h_number
    # st.write(f"입력한 숫자: {h_number}")     
    if h_number != 0:        
        if h_number < c_num:
            st.warning("예측한 값이 낮습니다.")
        elif h_number > c_num:
            st.warning("예측한 값이 높습니다.")
        else:
            st.balloons()
            st.success(f"정답! {c_num}였습니다.")
            del st.session_state.c_number    


def show_game2():    
    st.title("✊✌️🖐️ 가위바위보 게임")

    # 이미지 경로 (로컬)
    images = {
        0: r"C:\python_src\streamlit\가위.png",
        1: r"C:\python_src\streamlit\바위.png",
        2: r"C:\python_src\streamlit\보.png"
    }

    # 애니메이션용 GIF (컴퓨터가 생각하는 중)
    gif_url = "https://raw.githubusercontent.com/pia222sk20/python/main/streamlit/merged.gif"

    # 세션 초기화
    if "user_choice" not in st.session_state:
        st.session_state.user_choice = None
    if "comp_choice" not in st.session_state:
        st.session_state.comp_choice = None

    placeholder = st.empty()

    # 유저 선택 버튼
    col1, col2, col3 = st.columns(3)
    if col1.button("✌️ 가위"):
        st.session_state.user_choice = 0
    if col2.button("✊ 바위"):
        st.session_state.user_choice = 1
    if col3.button("🖐️ 보"):
        st.session_state.user_choice = 2

    # 유저 선택 전에는 GIF 애니메이션
    if st.session_state.user_choice is None:
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.write("👨 당신의 선택을 기다리는 중...")
            st.image(gif_url, width=300, use_container_width=True)
    else:
        # 유저 선택 후 컴퓨터 선택 랜덤 확정
        st.session_state.comp_choice = random.randint(0, 2)
        user = st.session_state.user_choice
        comp = st.session_state.comp_choice

        st.write("👨 당신의 선택")
        st.image(images[user], width=150)

        st.write("💻 컴퓨터의 선택")
        placeholder.image(images[comp], width=150)

        # 승부 판정
        if user == comp:
            st.info("🤝 비겼습니다!")
        elif (user == 0 and comp == 2) or (user == 1 and comp == 0) or (user == 2 and comp == 1):
            st.success("🎉 당신이 이겼습니다!")
        else:
            st.error("😢 졌습니다...")

        # 다시 시작 버튼
        if st.button("다시 시작", key="restart_button"):
            st.session_state.user_choice = None
            st.session_state.comp_choice = None
            st.rerun()

    
# 선택된 메뉴에 따라 해당하는 컨텐츠 표시
if selected_menu == "숫자맞추기":
    show_game1()
elif selected_menu == "가위바위보":
    show_game2()

