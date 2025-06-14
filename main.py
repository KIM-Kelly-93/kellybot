import streamlit as st

st.set_page_config(page_title="KellyBot", layout="centered")
st.title("🤖 KellyBot")

api_key = st.text_input("🔑 OpenAI API 키 입력", type="password")

if not api_key:
    st.warning("API 키를 입력해야 분석을 시작할 수 있습니다.")
    st.stop()

st.sidebar.title("📁 프로젝트 선택")
tab = st.sidebar.radio("원하는 기능을 선택하세요:", [
    "기업 분석",
    "우주 알림장",
    "업무 미팅 요약"
])

if tab == "기업 분석":
    st.header("📊 기업 분석")
    file = st.file_uploader("PDF 업로드", type=["pdf"])
    if file:
        st.success("업로드 완료! (분석 준비 중...)")

elif tab == "우주 알림장":
    st.header("✉️ 알림장 답장 생성기")
    note = st.text_area("알림장 내용 입력")
    if note:
        st.success("감동 답장 생성 중...")

elif tab == "업무 미팅 요약":
    st.header("📝 미팅 요약 정리")
    log = st.text_area("회의 기록 입력")
    if log:
        st.success("요약 준비 중...")
