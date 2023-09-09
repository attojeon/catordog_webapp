import streamlit as st 
import requests, random
from PIL import Image
from io import BytesIO

def reload():
    st.experimental_rerun()

st.set_page_config(
    page_title="고or강",
    page_icon="🐶"
)

choice = random.choice(["고양이", "강아지"])
if choice == "고양이":
    # 고양이 이미지 랜덤으로 가져오기
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    response_json = response.json()
    image_url = response_json[0]["url"]
else:
    # 강아지 이미지 랜덤으로 가져오기 
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    response_json = response.json()
    image_url = response_json["message"]


st.title("고양이 또는 강아지 🐶🐱")
st.button("고or강 새로고침")
st.image(image_url, caption=choice, use_column_width=True, width=400)

