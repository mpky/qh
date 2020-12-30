import streamlit as st
import numpy as np
import pandas as pd
import glob

st.title('QH App')

filenames = glob.glob('./QH/*.xlsx')
filenames.sort(reverse=True)



def load_data():

    # if sheet == './QH/Copy of لائحة المديونين.xlsx':
    sheet = st.selectbox('Which sheet would you like to search?',filenames)
    data = pd.read_excel(sheet, engine='openpyxl')
    data = data[data.columns[::-1]]

    return data
data = load_data()

name_search = st.text_input("Search for a name")

st.dataframe(data[data['اسم كامل'].str.contains(str(name_search), na=False)])
