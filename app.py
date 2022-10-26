# 각각의 동영상 조회수를 표시한다   
import streamlit as st
import pandas as pd

view = [100, 150, 30]

st.write('# Sangjun's page')
st.write("## raw")
view
st.write('## bar chart')
st.bar_chart(view)

sview = pd.Series(view)
sview
