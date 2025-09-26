# Streamlit 예제 프로젝트

이 저장소는 Streamlit을 사용한 다양한 웹 애플리케이션 예제를 포함하고 있습니다.

## 환경 설정

### 필요한 라이브러리 설치

```bash
pip install streamlit
pip install streamlit-autorefresh
```

### 가상환경 설정 (권장)

```bash
# 가상환경 생성
python -m venv streamlit_prj

# 가상환경 활성화
# Windows
streamlit_prj\Scripts\activate
# Linux/Mac
source streamlit_prj/bin/activate

# 필요한 라이브러리 설치
pip install streamlit streamlit-autorefresh
```

## 예제 파일 설명

### s_01.py - Streamlit 기본 UI 요소
- Streamlit의 기본적인 UI 컴포넌트 사용법 소개
- 타이틀, 헤더, 버튼, 체크박스, 라디오 버튼, 선택 상자, 슬라이더, 텍스트 입력 등 기본 위젯 예제

### s_02.py - 숫자 맞추기 게임
- 세션 상태를 사용한 간단한 숫자 맞추기 게임
- `st.session_state`를 활용한 상태 관리 예제
- 숫자 입력과 결과 확인 기능 구현

### s_03.py - 레이아웃과 데이터 표시
- 컬럼 레이아웃을 사용한 화면 구성
- 데이터 시각화와 표 표시 예제

### s_04.py - 파일 업로드와 처리
- 파일 업로드 기능 구현
- 업로드된 파일 처리와 결과 표시

### s_05.py - 데이터 시각화
- 차트와 그래프를 활용한 데이터 시각화
- 다양한 시각화 라이브러리 활용 예제

### s_06.py - 인터랙티브 게임 (가위바위보)
- 사이드바를 활용한 메뉴 구성
- 세션 상태를 활용한 게임 상태 관리
- 이미지와 애니메이션 사용
- 컬럼 레이아웃을 활용한 반응형 디자인
- 실시간 상호작용과 결과 표시

## 실행 방법

각 예제는 다음 명령어로 실행할 수 있습니다:

```bash
streamlit run streamlit/[파일명].py

# 예시
streamlit run streamlit/s_01.py
streamlit run streamlit/s_06.py
```

## 주요 기능

- **세션 상태 관리**: `st.session_state`를 사용한 상태 관리
- **반응형 레이아웃**: 컬럼과 컨테이너를 활용한 화면 구성
- **인터랙티브 요소**: 버튼, 입력 필드, 선택 상자 등
- **데이터 시각화**: 차트, 그래프, 테이블 표시
- **파일 처리**: 파일 업로드와 데이터 처리
- **애니메이션**: 게임과 상호작용에 사용되는 시각적 효과

## 참고 사항

- 모든 예제는 Python 3.6 이상에서 테스트되었습니다.
- 일부 예제는 추가 라이브러리가 필요할 수 있습니다.
- 실행 전 가상환경 활성화를 권장합니다.
- 코드 내 주석을 참고하여 각 기능의 세부 사항을 확인할 수 있습니다.

## 문제 해결

### 자주 발생하는 문제

1. **ModuleNotFoundError**
   ```bash
   pip install [부족한 라이브러리]
   ```

2. **Permission Error**
   - 가상환경이 제대로 활성화되었는지 확인
   - 관리자 권한으로 실행 필요 여부 확인

3. **Port 충돌**
   - 이미 실행 중인 Streamlit 앱 종료
   - 다른 포트 번호로 실행: `streamlit run app.py --server.port [포트번호]`