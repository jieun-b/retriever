import streamlit as st

# 브라우저 탭에 표시될 제목과 레이아웃 설정
st.set_page_config(page_title="Food Retriever", layout="wide")

# 웹 페이지 상단에 제목 표시
st.title("🍲 Food Retriever Demo")
# 텍스트 출력
st.write("Upload a food image and retrieve related recipes or information.")

# 화면 오른쪽/왼쪽(기본 왼쪽)에 사이드바 렌더링
with st.sidebar:
    st.header("Options")
    st.info("This is a demo version. Results are placeholders until RAG pipeline is connected.")

# 레이아웃: 2 컬럼 (왼쪽 업로드, 오른쪽 결과), 비율 1:2
col1, col2 = st.columns([1, 2])

with col1:
    # 이미지 파일을 업로드할 수 있는 버튼을 생성
    uploaded = st.file_uploader("Upload a food image", type=["jpg", "png"])

    if uploaded:
        # 업로드된 이미지를 웹 화면에 표시, 이미지 아래에 캡션 추가, 이미지가 컬럼 너비에 맞춰 자동 조정
        st.image(uploaded, caption="Uploaded Image", use_container_width=True)

with col2:
    # 소제목 표시
    st.subheader("🔍 Search Results")
    if uploaded:
        # 실제 RAG 연결 전 placeholder
        st.success("Top Match: 🍕 Pizza")
        st.write("**Recipe:** Dough, tomato sauce, cheese, toppings...")
    else:
        st.warning("Please upload an image to see results"
        ".")