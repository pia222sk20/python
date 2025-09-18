import streamlit as st
import pandas as pd
import shopv1

datas = shopv1.readAll_customers()
st.set_page_config(layout="wide")

# 초기 회원 데이터
if "members" not in st.session_state:
    st.session_state.members = pd.DataFrame(
    #     [
    #     {"회원아이디": "user01", "회원이름": "홍길동"},
    #     {"회원아이디": "user02", "회원이름": "이몽룡"},
    #     {"회원아이디": "user03", "회원이름": "성춘향"}
    # ]
    datas
    )

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
        for i, row in st.session_state.members.iterrows():
            col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
            with col1:
                print('***********', row["회원아이디"])                
                if st.button(str(row["회원아이디"]), key=f"id_{i}"):
                    st.session_state.selected_member_index = i
            with col2:
                if st.button(row["회원이름"], key=f"name_{i}"):
                    st.session_state.selected_member_index = i
            # with col3:
            #     if st.button("수정", key=f"edit_{i}"):
            #         st.session_state.selected_member_index = i
            #         st.info(f"{row['회원이름']} 수정 준비")
            # with col4:
            #     if st.button("삭제", key=f"del_{i}"):
            #         st.session_state.members = st.session_state.members.drop(i).reset_index(drop=True)
            #         st.success(f"{row['회원이름']} 삭제됨")
            #         st.session_state.selected_member_index = None
            #         st.experimental_rerun()

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
                    st.success("회원정보 수정 완료")
                    st.experimental_rerun()
                else:
                    st.session_state.members.loc[len(st.session_state.members)] = {"회원아이디": member_id, "회원이름": member_name}
                    st.success("신규 회원 추가 완료")
                    st.experimental_rerun()
        with col_b:
            if st.button("입력 초기화"):
                st.session_state.selected_member_index = None
                st.rerun()
