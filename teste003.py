import streamlit as st
import pandas as pd

arquivo = st.file_uploader('Enviar CSV')

if arquivo:
    df = pd.read_csv(arquivo)
    st.dataframe(df)

    st.download_button(
        'Baixar dados',
        data=df.to_csv(index=False),
        file_name="dados.csv"
    )
