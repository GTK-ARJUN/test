import streamlit as st
import numpy as np
import pandas as pd

st.title('Victory through learning  and courage')


st.header('This is echoed data')
with st.echo():
    x=54
    y=100


@st.cache(suppress_st_warning=True)
def expensive_computation(a,b):
    st.write("Cache miss: expensive_computation(", a, ",", b, ") ran")
    return a * b

a=2
b=st.slider('Pick a number ',0,10)
res=expensive_computation(a,b)

st.write('result', res)


x=st.number_input("Enter a number here")

st.write(x)