import streamlit as st
import pandas as pd
st.title("Streamlit Text input")

name = st.text_input("Enter your name: ")
#slider
age=st.slider("Select your age: ",0,100,25)
st.write(f"Your age is {age}")
#selectbox
options = ["Python","Java","C++","Javascript"]
choice = st.selectbox(f"Choose your favourite language:",options)
st.write(f"You've selected {choice}")
if name:
    st.write(f"Hello, {name}")

data={
    "Name": ["John","Mridul","Jake","CJill"],
    "Age" : [20,25,5,6],
    "City" : ["Chittagong", "Dhaka","B arisal", "Saidpur"]
}
df = pd.DataFrame(data)
st.write(df)
df.to_csv("sample_Data.csv")
uploaded_files = st.file_uploader("Choose a CSV file:",type="CSV")

if uploaded_files is not None:
    df =pd.read_csv(uploaded_files)
    st.write(df)
