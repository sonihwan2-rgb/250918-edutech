import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# --- Streamlit 주요 요소 예시 ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 제목과 텍스트
st.header("헤더 예시")  # 큰 제목
st.subheader("서브헤더 예시")  # 작은 제목
st.text("일반 텍스트 예시")  # 일반 텍스트

# 2. 마크다운
st.markdown("**마크다운 텍스트**: *굵게*, _기울임_, [링크](https://streamlit.io)")  # 마크다운 지원

# 3. 코드 및 수식
st.code("print('Hello Streamlit!')", language='python')  # 코드 블록
st.latex(r"\int_a^b f(x)dx")  # LaTeX 수식

# 4. 데이터프레임 및 테이블
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
st.dataframe(df)  # 데이터프레임 표시
st.table(df)  # 테이블 표시

# 5. 차트 및 그래프
st.line_chart(np.random.randn(20, 3))  # 라인 차트
st.bar_chart(np.random.randn(20, 3))  # 바 차트
st.area_chart(np.random.randn(20, 3))  # 영역 차트

# 6. Matplotlib 차트
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
st.pyplot(fig)  # Matplotlib 그래프

# 7. 입력 위젯
st.text_input("텍스트 입력")  # 텍스트 입력
st.text_area("텍스트 영역")  # 여러 줄 텍스트 입력
st.number_input("숫자 입력", min_value=0, max_value=100, value=50)  # 숫자 입력
st.date_input("날짜 입력")  # 날짜 입력
st.time_input("시간 입력")  # 시간 입력
st.file_uploader("파일 업로드")  # 파일 업로드

# 8. 선택 위젯
st.checkbox("체크박스")  # 체크박스
st.radio("라디오 버튼", ["A", "B", "C"])  # 라디오 버튼
st.selectbox("셀렉트박스", ["A", "B", "C"])  # 셀렉트박스
st.multiselect("멀티셀렉트", ["A", "B", "C"])  # 멀티셀렉트

# 9. 슬라이더
st.slider("슬라이더", min_value=0, max_value=100, value=25)  # 슬라이더
st.select_slider("셀렉트 슬라이더", options=["A", "B", "C"])  # 셀렉트 슬라이더

# 10. 버튼
st.button("버튼")  # 버튼
with st.form("폼 예시"):
    st.form_submit_button("폼 제출")  # 폼 제출 버튼

# 11. 이미지, 오디오, 비디오
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지")  # 이미지 표시
st.audio(np.random.randn(44100), format='audio/wav')  # 오디오 표시 (임의 데이터)
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오 표시

# 12. 진행바, 스피너, 경고
st.progress(70)  # 진행바
with st.spinner("로딩 중..."):
    st.write("스피너 예시")  # 스피너
st.success("성공 메시지")  # 성공 메시지
st.info("정보 메시지")  # 정보 메시지
st.warning("경고 메시지")  # 경고 메시지
st.error("에러 메시지")  # 에러 메시지

# 13. 사이드바
st.sidebar.title("사이드바 제목")  # 사이드바 제목
st.sidebar.button("사이드바 버튼")  # 사이드바 버튼

# 14. 상태 표시
st.caption("캡션 예시")  # 캡션
st.write("write 함수는 다양한 타입을 자동으로 렌더링합니다.")  # write 함수

# 15. 기타
st.json({"key": "value", "number": 123})  # JSON 표시
st.metric(label="온도", value="25°C", delta="1°C")  # 메트릭 표시

# 각 요소마다 주석으로 설명을 달았습니다.
