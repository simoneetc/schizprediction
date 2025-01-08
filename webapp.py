import streamlit as st
import pickle
import pandas as pd
import sklearn 
print(sklearn.__version__)
# Load the saved pipeline model


with open('voting_pipeline_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app header
st.title('Model Prediction App')

# Feature inputs
st.header('Enter feature values:')
gender = st.selectbox('Gender', ['Male', 'Female'])
marital_status = st.selectbox('Marital Status', ['Single', 'Married','Widowed'])
age = st.number_input('Age', min_value=18, max_value=100, value=30)
fatigue = st.text_input('Fatigue', value="0.0363237389187373")
slowing = st.text_input('Slowing', value="0.5808079689048639")
pain = st.text_input('Pain', value="0.0053555198838411")
hygiene = st.text_input('Hygiene', value="0.3069676027888867")
movement = st.text_input('Movement', value="0.8136175955953819")

# Converting string inputs to float after they are entered
try:
    fatigue = float(fatigue)
    slowing = float(slowing)
    pain = float(pain)
    hygiene = float(hygiene)
    movement = float(movement)
except ValueError:
    st.error("Please enter valid float values.")




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
    # if(prediction==1):
    #     st.write('Not On the Schiznophrenic spectrum')
    # else:
    #     st.write('Not on the Schiznophrenic spectrum')
    if(prediction==1):
        st.write("Elevated proneness")
    elif(prediction==2) :
        st.write("High Proness")
    elif(prediction==3):
        st.write("Moderate Proneness")
    elif(prediction==4):
        st.write("Low proneness/not on the spectrum")
    else:
        st.write("Very High Proneness")


        
        

