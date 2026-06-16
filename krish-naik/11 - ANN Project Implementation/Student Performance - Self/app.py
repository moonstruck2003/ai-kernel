import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import pickle

## load the trained model
model = tf.keras.models.load_model('model.h5')

## load the encoder and sclaer

with open('Standard_Scaler.pkl','rb') as file:
    scaler = pickle.load(file)
with open('ethnicity_encoder.pkl','rb') as file:
    encoder = pickle.load(file)

## streamlit app
st.title("Student Performance Prediction")\
##User input
age = st.slider('Age', 15, 25)
gender = st.selectbox('Gender', [0, 1])
ethnicity = st.selectbox('Ethnicity', [0, 1, 2, 3, 4])
parental_education = st.slider('Parental Education', 0, 4)
study_time_weekly = st.number_input('Study Time Weekly')
absences = st.slider('Absences', 0, 93)
tutoring = st.selectbox('Tutoring', [0, 1])
parental_support = st.slider('Parental Support', 0, 4)
extracurricular = st.selectbox('Extracurricular', [0, 1])
sports = st.selectbox('Sports', [0, 1])
music = st.selectbox('Music', [0, 1])
volunteering = st.selectbox('Volunteering', [0, 1])

##input data

input_data = pd.DataFrame({

    "Age": [age],
    "Gender": [gender],
    "ParentalEducation": [parental_education],
    "StudyTimeWeekly": [study_time_weekly],
    "Absences": [absences],
    "Tutoring": [tutoring],
    "ParentalSupport": [parental_education], 
    "Extracurricular": [extracurricular],
    "Sports": [sports],
    "Music": [music],
    "Volunteering": [volunteering]
     
})

## ethnicity encoder 

ethnicity_encoded = encoder.transform([[ethnicity]]).toarray()
ethnicity_encoded_df = pd.DataFrame(ethnicity_encoded,columns=encoder.get_feature_names_out(['Ethnicity']))

input_data = pd.concat([input_data.reset_index(drop=True),ethnicity_encoded_df],axis=1)

## scale the input data

input_data_scaled = scaler.transform(input_data)

## prediction GPA

prediction = model.predict(input_data_scaled)

prediction_proba = prediction[0][0]

st.write(f"Predicted GPA: {prediction_proba}")
