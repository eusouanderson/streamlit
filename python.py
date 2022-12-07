import streamlit as st
import pandas as pd
pessoas = dict()

st.title('-----')
st.markdown('Ola ...... ')
st.header('Ola')

pessoas['nome'] = st.text_input('Digite seu nome')

if not pessoas['nome']:
  st.warning('Por favor insira seu nome!')
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





