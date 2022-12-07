import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
pessoas = dict()

st.title('Amigo Secreto 2022')
pessoas['nome'] = st.text_input('Digite seu nome')

if not pessoas['nome']:
  st.warning('Por favor insira seu nome!')
  st.stop()
st.success('Obrigado!')

pessoas['presente'] = st.text_input('Digite qual presente você quer ganhar ')
pessoas['link'] = st.text_input('Cole aqui um link')
pessoas['img'] = st.file_uploader('Upload de uma print ou foto do seu presente ')

df =pd.DataFrame(
        pessoas,
        columns=[pessoas['nome'], pessoas['presente'], pessoas['link'], pessoas['img']])

if st.button('enviar'):
    print('Ola')
    st.table(df)
    st.balloons()


col_a, col_b = st.columns(2)





