import streamlit as st
import pickle
import pandas as pd
import sklearn 
print(sklearn.__version__)
# Load the saved pipeline model


with open('/voting_pipeline_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app header
st.title('Model Prediction App')

# Feature inputs
st.header('Enter feature values:')
gender = st.selectbox('Gender', ['Male', 'Female'])
marital_status = st.selectbox('Marital Status', ['Single', 'Married'])
age = st.number_input('Age', min_value=18, max_value=100, value=30)
fatigue = st.slider('Fatigue', min_value=0, max_value=10, value=5)
slowing = st.slider('Slowing', min_value=0, max_value=10, value=5)
pain = st.slider('Pain', min_value=0, max_value=10, value=5)
hygiene = st.slider('Hygiene', min_value=0, max_value=10, value=5)
movement = st.slider('Movement', min_value=0, max_value=10, value=5)

# Prepare the input data as a DataFrame
input_data = pd.DataFrame({
    'Gender': [gender],
    'Marital_Status': [marital_status],
    'Age': [age],
    'Fatigue': [fatigue],
    'Slowing': [slowing],
    'Pain': [pain],
    'Hygiene': [hygiene],
    'Movement': [movement]
})

# Button for prediction
if st.button('Predict'):
    # Make the prediction
    prediction = model.predict(input_data)
    
    # Display the prediction result
    st.subheader('Prediction Result:')
    # st.write(f'The predicted value is: {prediction[0]}')
    if(prediction>2):
        st.write('On the Schiznophrenic spectrum')
    else:
        st.write('Not on the Schiznophrenic spectrum')