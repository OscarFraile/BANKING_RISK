import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

#INPUT

df = sns.load_dataset('tips')

seleccion_sexo = st.selectbox('Elige sexo:',['Male','Female'])

seleccion_fumador = st.radio('Elige fumador:',['Yes','No'])

slider_total_cuenta = st.slider('Cuenta mayor que: ', df.total_bill.min(), df.total_bill.max())


#CALCULOS

datos = df.loc[(df.sex == seleccion_sexo) & 
                      (df.smoker == seleccion_fumador) & 
                      (df.total_bill > slider_total_cuenta)].copy()

ticket_medio = round(datos.total_bill.mean(),2)


#OUTPUT

kpi_ticket_medio = st.metric('Ticket Medio',ticket_medio)

fig, ax = plt.subplots()

ax = sns.histplot(data = datos, x = 'total_bill')

st.pyplot(fig)