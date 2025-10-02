import streamlit as st
import pandas as pd
import shopdbmng

st.set_page_config(layout="wide")

# --- 초기 상태 설정 ---
if "members" not in st.session_state:
    st.session_state.members = pd.DataFrame(columns=["회원아이디", "회원이름"])
if "selected_member_index" not in st.session_state:
    st.session_state.selected_member_index = None
if "show_list" not in st.session_state:
    st.session_state.show_list = False

# 좌우 레이아웃
left_col, right_col = st.columns([1, 3])

# --- 왼쪽: 리스트 보기 버튼 ---
with left_col:
    st.header("회원")
    if st.button("회원 리스트 보기"):
        datas = shopdbmng.readAll_customers()
        st.session_state.members = pd.DataFrame(datas)
        st.session_state.show_list = True
        # 초기화
        st.session_state.selected_member_index = None
        for key in ["edit_id", "edit_name", "new_id", "new_name"]:
            st.session_state.pop(key, None)
        st.rerun()

# --- 오른쪽: 리스트 & 입력폼 ---
with right_col:
    st.header("회원 리스트")
    if st.session_state.show_list:
        st.table(st.session_state.members)

        # 선택박스 (처음엔 "선택하세요" 가 보임)
        selected_member = st.selectbox(
            "회원 선택",
            options=[None] + list(range(len(st.session_state.members))),
            format_func=lambda x: "선택하세요" if x is None else f"{st.session_state.members.iloc[x]['회원아이디']} - {st.session_state.members.iloc[x]['회원이름']}",
            index=0
        )

        # 선택 반영
        st.session_state.selected_member_index = selected_member

        st.divider()

        # 입력폼
        if st.session_state.selected_member_index is not None:
            sel = st.session_state.members.iloc[st.session_state.selected_member_index]
            member_id = st.text_input("회원아이디", value=sel["회원아이디"], key="edit_id")
            member_name = st.text_input("회원이름", value=sel["회원이름"], key="edit_name")
        else:
            member_id = st.text_input("회원아이디", value="", key="new_id")
            member_name = st.text_input("회원이름", value="", key="new_name")

        # 버튼들
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("수정/저장"):
                if st.session_state.selected_member_index is not None:
                    # 수정
                    idx = st.session_state.selected_member_index
                    old_member_id = st.session_state.members.at[idx, "회원아이디"]
                    shopdbmng.update_customer(old_member_id, member_name)
                else:
                    # 신규
                    shopdbmng.create_customer(member_name)

                # DB에서 다시 조회
                datas = shopdbmng.readAll_customers()
                st.session_state.members = pd.DataFrame(datas)

                # 초기화
                st.session_state.selected_member_index = None
                for key in ["edit_id", "edit_name", "new_id", "new_name"]:
                    st.session_state.pop(key, None)

                st.rerun()

        with col_b:
            if st.button("입력 초기화"):
                st.session_state.selected_member_index = None
                for key in ["edit_id", "edit_name", "new_id", "new_name"]:
                    st.session_state.pop(key, None)
                st.rerun()
