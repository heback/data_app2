import streamlit as st

st.title('Hello World!')

name = 'Jungu Lee'

st.text(f'My name is {name}')

st.markdown('This is **markdown**')

import pandas as pd
df = pd.read_csv('data/iris.csv')

st.dataframe(df)