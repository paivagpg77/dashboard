import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt

st.title('📊 Dashboard de Vendas')

dados = {
    'Mês' : ['Jan', 'Fev ' , 'Mar' ,'Abr'],
    'Vendas' : [1000 , 1550 , 1330 ,1322] 
}

df = pd.DataFrame(dados)
st.dataframe(df)

#Gráfico
plt.plot(df['Mês'] , df['Vendas'])
plt.xlabel('Mês')
plt.xlabel('Vendas')
st.pyplot(plt)