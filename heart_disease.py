import pickle 
import streamlit as st 
from streamlit_option_menu import option_menu

# loading the saved model
heart_disease_model = pickle.load(open('/Users/oluwaseyiakinsanya/Desktop/Predictive_Analytics/heart-disease-predictor-xm/saved model/heart_disease_model.sav', 'rb'))

# page title
st.title('Heart Disease Prediction using ML')

# information section for input ranges
st.markdown("### Input Guidelines for Accurate Prediction")
st.markdown("""
- **Age:** 18 – 100 years  
- **Sex:** 0 = female, 1 = male  
- **Chest Pain Types (CP):** 0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic  
- **Resting Blood Pressure (Trestbps):** 94 – 200 mm Hg  
- **Serum Cholesterol (Chol):** 126 – 564 mg/dL  
- **Resting Electrocardiographic Results (Restecg):** 0 = normal, 1 = ST-T wave abnormality, 2 = left ventricular hypertrophy  
- **Maximum Heart Rate (Thalach):** 71 – 202 bpm  
- **Exercise Induced Angina (Exang):** 0 = no, 1 = yes  
- **Oldpeak:** 0.0 – 6.2 (ST depression induced by exercise relative to rest)  
- **Slope of ST Segment (Slope):** 0 = upsloping, 1 = flat, 2 = downsloping  
""")

# getting the input data from the user
col1, col2 = st.columns(2)

with col1:
    Age = st.text_input('Age')
    
with col2:
    Sex = st.text_input('Sex (0 = female, 1 = male)')
        
with col1:
    CP = st.text_input('Chest Pain Type (0–3)')
        
with col2:
    Trestbps = st.text_input('Resting Blood Pressure (mm Hg)')
        
with col1:
    Chol = st.text_input('Serum Cholesterol (mg/dL)')
        
with col2:
    Restecg = st.text_input('Resting ECG (0–2)')
    
with col1:
    Thalach = st.text_input('Maximum Heart Rate (bpm)')
        
with col2:
    Exang = st.text_input('Exercise Induced Angina (0 = no, 1 = yes)')
        
with col1:
    Oldpeak = st.text_input('ST Depression (Oldpeak)')
        
with col2:
    Slope = st.text_input('Slope (0 = upsloping, 1 = flat, 2 = downsloping)')

# code for prediction 
heart_diagnosis = ''
    
# creating a button for prediction
if st.button('Heart Disease Test Result'):
    try:
        # convert inputs to float or int
        input_data = [[
            float(Age), int(Sex), int(CP), float(Trestbps), float(Chol),
            int(Restecg), float(Thalach), int(Exang), float(Oldpeak), int(Slope)
        ]]
        
        heart_disease_prediction = heart_disease_model.predict(input_data)
        
        if heart_disease_prediction[0] == 1:
            heart_diagnosis = 'The person **has** heart disease.'
        else:
            heart_diagnosis = 'The person **does not have** heart disease.'
    except ValueError:
        heart_diagnosis = '⚠ Please enter valid numerical inputs for all fields.'

st.success(heart_diagnosis)
