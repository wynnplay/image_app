import streamlit as st
from rembg import remove
from PIL import Image

from streamlit_image_comparison import image_comparison
import easyocr as ocr #ocr
import numpy as np  

st.set_page_config(page_title='My_First_Image_App', layout="centered")
st.subheader('[미니프로젝트] 이미지 배경제거 서비스 + 글자추출 웹서비스')
st.markdown('### :arrow_forward::sunglasses: Remove Background - `rmbg`')
st.markdown("#### sample result") 

image-comparison(
    img1 = "https://raw.githubusercontent.com/wynnplay/image_app/main/woman.jpeg", 
    img2 = "https://raw.githubusercontent.com/wynnplay/image_app/main/woman_rmbg.png",
    label1 = "원본 이미지", 
    label2 = '배경제거 이미지", 
    show_labels = True, 
    make-responsive=True, 
    in_memory=True)  
    
st.markdown("### :arrow_forward: :ab:글자 추출(OCR) - `easyocr`")  

option = st.selectbox(
    '어떤 서비스를 원하시나요?',
    ('배경제거','글자추출')) 

st.info(f'당신의 선택은: {option}')
if option == '배경제거': 
    uploaded_file = st.file_uploader("이미지를 업로드하세요", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    input = Image.open(uploaded_file)
    st.image(input_, caption='원본 이미지', use_column_width=True)
    with st.spinner("열심히 작업 중 ......"): 
        output = remove(input_) 
        st.image(output, caption='배경 제거 이미지', use_column_width=True)


if option =='글자추출': 
    image = st.file_uploader(labkel = 'Uplead your image here", type=['png,'jpg', 'jpeg'])
    @st.cache
    def laod_model():
        reader = ocr.Reader(['ko','en'],model_storage_directory='-')
        return reader 

    reder = load_model() 

    if image is not None: 
        input_image = Image.open(image) 
        st.image(input_image) 

        with st.spinner("AI is at work!"): 
        
    


