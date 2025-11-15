import streamlit as st
from PIL import Image

# 웹툰 이미지 파일 경로 (여기에 웹툰 이미지를 업로드하거나 경로를 설정)
webtoon_images = [
    "webtoon1.jpg",  # 1화 이미지
    "webtoon2.jpg",  # 2화 이미지
    "webtoon3.jpg",  # 3화 이미지
    "webtoon4.jpg",  # 4화 이미지
    # 추가적인 웹툰 이미지 경로
]

# 웹툰 제목
st.title("📖 웹툰 보기 앱")

# 웹툰 슬라이드 (이미지 넘기기)
current_chapter = st.slider("화 선택", 1, len(webtoon_images), 1)

# 웹툰 이미지 출력
webtoon_image = Image.open(webtoon_images[current_chapter - 1])
st.image(webtoon_image, caption=f"웹툰 {current_chapter}화", use_column_width=True)

# 설명 (선택 사항)
st.write(f"현재 보고 있는 웹툰은 **{current_chapter}화**입니다. 웹툰을 즐겨보세요!")
