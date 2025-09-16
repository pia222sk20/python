import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Streamlit 레이아웃 예제",
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
def show_game1():
    st.header("숫자맞추기")
    st.write("환영합니다! 이곳은 숫자맞추기 게임 페이지입니다.")
def show_game2():
    st.header("가위바위보")
    st.write("환영합니다! 이곳은 가위바위보 게임 페이지입니다.")        
    
# 선택된 메뉴에 따라 해당하는 컨텐츠 표시
if selected_menu == "숫자맞추기":
    show_game1()
elif selected_menu == "가위바위보":
    show_game2()

