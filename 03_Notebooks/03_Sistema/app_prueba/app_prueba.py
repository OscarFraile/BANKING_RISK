import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import time

archivo = st.file_uploader('Selecciona un archivo csv')

if archivo is not None:
    df = pd.read_csv(archivo)
    time.sleep(5)
    
else:
    st.stop()

variable_num = st.selectbox('Selecciona una variable numerica:',df.columns.to_list())

fig, ax = plt.subplots()

ax = sns.histplot(data = df, x = variable_num)

st.pyplot(fig)