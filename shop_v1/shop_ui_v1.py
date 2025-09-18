import streamlit as st
import pandas as pd
import shopv1

st.set_page_config(layout="wide")

# 초기 회원 데이터
if "members" not in st.session_state:
    datas = shopv1.readAll_customers()
    st.session_state.members = pd.DataFrame(datas)

# 현재 선택된 회원
if "selected_member_index" not in st.session_state:
    st.session_state.selected_member_index = None

# 좌우 레이아웃
left_col, right_col = st.columns([1, 3])

# ------------------------------------------
# ① 왼쪽: 회원 버튼 → 누르면 오른쪽 리스트 출력
# ------------------------------------------
with left_col:
    st.header("회원")
    if st.button("회원 리스트 보기"):
        st.session_state.show_list = True

# ------------------------------------------
# ② 오른쪽: 회원 리스트 & 입력폼
# ------------------------------------------
with right_col:
    st.header("회원 리스트")

    if st.session_state.get("show_list", False):
        # 회원 리스트 테이블
        st.table(st.session_state.members)
        
        # 회원 선택을 위한 셀렉트박스
        selected_member = st.selectbox(
            "회원 선택",
            options=range(len(st.session_state.members)),
            format_func=lambda x: f"{st.session_state.members.iloc[x]['회원아이디']} - {st.session_state.members.iloc[x]['회원이름']}",
            key="member_selector"
        )
        
        if selected_member is not None:
            st.session_state.selected_member_index = selected_member

        st.divider()

        # ③ 아래 입력창: 선택된 회원 데이터 채우기
        if st.session_state.selected_member_index is not None:
            selected = st.session_state.members.iloc[st.session_state.selected_member_index]
            member_id = st.text_input("회원아이디", selected["회원아이디"], key="edit_id")
            member_name = st.text_input("회원이름", selected["회원이름"], key="edit_name")
        else:
            member_id = st.text_input("회원아이디", key="new_id")
            member_name = st.text_input("회원이름", key="new_name")

        # ④ 수정 / 저장 버튼
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("수정/저장"):
                if st.session_state.selected_member_index is not None:
                    st.session_state.members.at[st.session_state.selected_member_index, "회원아이디"] = member_id
                    st.session_state.members.at[st.session_state.selected_member_index, "회원이름"] = member_name
                    print('****',member_id,member_name,type(member_id), type(member_name))
                    shopv1.update_customer(member_id,member_name)
                    st.rerun()
                else:
                    st.session_state.members.loc[len(st.session_state.members)] = {"회원아이디": member_id, "회원이름": member_name}
                    # 데이터 추가 로직
                    shopv1.create_customer(member_name)
                    del st.session_state.members
                    st.rerun()
        with col_b:
            if st.button("입력 초기화"):
                st.session_state.selected_member_index = None
                st.rerun()
