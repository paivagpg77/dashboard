import streamlit as st
import pandas as pd
import os

arquivo = "usuarios.csv"

nome = st.text_input('Nome')
idade = st.number_input('Idade', min_value=0)

if st.button('Salvar'):
    novo = pd.DataFrame([[nome , idade]] , columns=['Nome' , 'Idade'])

    if os.path.exists(arquivo):
        novo.to_csv(arquivo, mode='a', header=False , index=False)
    else:
        novo.to_csv(arquivo , index=False)

    st.success("Dados Salvos!")