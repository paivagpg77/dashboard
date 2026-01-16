import streamlit as st
import sqlite3 as sql 

conn = sql.connect('dados.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
               nome TEXT ,
               idade INTEGER
)
""")
conn.commit()

nome = st.text_input('Nome')
idade = st.number_input('Idade', min_value=0)

if st.button('Salvar'):
    cursor.execute(
        "INSERT INTO usuarios VALUES (?,?)" ,
        (nome , idade )
    )

    conn.commit()
    st.success("Dados salvos com sucesso!")