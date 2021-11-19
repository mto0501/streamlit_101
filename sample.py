import streamlit as st
import pandas as pd
import numpy as np
import cv2

menu = ["Home","About Me", "Read Data","Camera"]

choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    st.write("Hello World")
    st.header("First webapp")

    st.image("media\dog-beach-lifesaver.png")
    st.image("media\isle_of_dog.gif")
    st.video("media\dogs.mp4")
    

    col1,col2 = st.columns(2)
    with col1:
        dog_name = st.text_input("What is your dog name? ")
        st.write("Your dog name: ",dog_name)
    with col2:
        age = st.slider("Dog age", min_value=1, max_value=100)
        st.write("Your dog age: ",age)
elif choice == "Read Data":
    df = pd.read_csv("media\AB_NYC_2019.csv")
    st.dataframe(df)
elif choice == "About Me":
    st.audio("media\Impact_Moderato.mp3")

    fileUp = st.file_uploader("Upload file",type=["jpg","png","jpeg"]) # chỉ up đc 200 mb
    st.image(fileUp)
    # model.predict(fileUp)
elif choice == "Camera":
    st.title('Open your webcam')
    st.warning('Webcam show on local computer ONLY')
    show = st.checkbox('Show!')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0) # device 1/2

    while show:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        camera.release()
    




