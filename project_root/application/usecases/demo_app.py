import streamlit as st
import numpy as np
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from domain.ports.img_processor import process


st.header("Interfaz de demostracion para conversion imagen-LaTex usando IA")
im = st.file_uploader("Upload Image to process", ["jpg","jpeg", "png"])
col1, col2 =st.columns(2)


try:
    if im is not None:
        with col1:
            im_show = st.image(im, caption="imagen original")
            # st.write(type(im))
            im_procesada = process(im)
        
        with col2:
            im_proces = st.image(im_procesada, caption="imagen pre-procesada")

        tex = st.subheader("Prediccion a LaTex")
            
except RuntimeError as e:
    pass