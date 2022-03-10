import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
def set_bg_hack_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://ghantee.com/wp-content/uploads/2020/07/tree-wallpaper-illustration-fantasy-HD.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
set_bg_hack_url()
st.write("""
          # Steel  Defect Detection
          """
          )
upload_file = st.sidebar.file_uploader("Upload Cell Images", type="jpg")
Generate_pred=st.sidebar.button("Predict")
model=tf.keras.models.load_model('steel_model1.h5')
def import_n_pred(image_data, model):
    size = (120,120)
    image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img = np.asarray(image)
    reshape=img[np.newaxis,...]
    pred = model.predict(reshape)
    return pred
if Generate_pred:
    image=Image.open(upload_file)
    with st.expander('Steel Image', expanded = True):
        st.image(image, use_column_width=True)
    pred=import_n_pred(image, model)
    labels = ['Class-1', 'Class-2','Class-3','Class-4']
    st.title("Prediction of image is {}".format(labels[np.argmax(pred)]))