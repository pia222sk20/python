import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Streamlit 레이아웃 예제",
    layout="wide"  # 전체 페이지를 wide 모드로 설정
)

# 사이드바 메뉴 생성
with st.sidebar:
    st.title("메뉴")
    selected_menu = st.radio(
        "원하시는 메뉴를 선택하세요:",
        ["홈", "대시보드", "설정", "도움말"]
    )

# 메인 컨텐츠 영역
def show_home():
    st.header("홈")
    st.write("환영합니다! 이곳은 홈 페이지입니다.")
    
def show_dashboard():
    st.header("대시보드")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="온도", value="24°C", delta="1.2°C")
    with col2:
        st.metric(label="습도", value="80%", delta="-5%")
    
def show_settings():
    st.header("설정")
    st.text_input("사용자 이름")
    st.slider("알림 주기", 0, 100, 50)
    
def show_help():
    st.header("도움말")
    st.write("도움이 필요하시다면 아래 연락처로 문의해주세요:")
    st.write("이메일: help@example.com")

# 선택된 메뉴에 따라 해당하는 컨텐츠 표시
if selected_menu == "홈":
    show_home()
elif selected_menu == "대시보드":
    show_dashboard()
elif selected_menu == "설정":
    show_settings()
elif selected_menu == "도움말":
    show_help()
