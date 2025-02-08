import pickle
import pandas as pd
import streamlit as st

# Page config
st.set_page_config(page_title='Insurance Prediction')

# Page title
st.title('Insurance Prediction')

# -- Parameters -- #

age = st.number_input(label='Age', value=18, min_value=18, max_value=120)
bmi = st.number_input(label='BMI', value=30.)
children = st.slider(label='Children', min_value=0, max_value=5)
smoker = st.selectbox(label='Smoker', options=['no','yes'])

# -- Model -- #

with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def prediction():
    df_input = pd.DataFrame([{
        'age': age,
        'bmi': bmi,
        'children': children,
        'smoker': smoker
    }])
    prediction = model.predict(df_input)[0]
    return prediction

if st.button('Predict'):
    insurance_cost = prediction()
    st.success(insurance_cost)
