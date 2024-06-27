# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:36:55 2024

@author: CHAHATI DAYAL
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the Saved Models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
breast_model = pickle.load(open('Breast_Cancer_model.sav', 'rb'))

# SideBar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Breast Cancer Prediction'],
                           
                           icons=['activity', 'heart', 'people-fill' , 'gender-female'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')
    
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    diab_diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The Person is Diabetic'
            else:
                diab_diagnosis = 'The Person is not Diabetic'
        except ValueError:
            diab_diagnosis = 'Please enter valid numeric values'
            
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    heart_diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_disease_model.predict([[float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid numeric values'
            
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP_Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP_Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP_Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP_Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP_Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP_RAP')
    with col2:
        PPQ = st.text_input('MDVP_PPQ')
    with col3:
        DDP = st.text_input('Jitter_DDP')
    with col4:
        Shimmer = st.text_input('MDVP_Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP_Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer_APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer_APQ5')
    with col3:
        APQ = st.text_input('MDVP_APQ')
    with col4:
        DDA = st.text_input('Shimmer_DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')
    
    parkinsons_diagnosis = ''
    
    # Creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        try:
            parkinsons_prediction = parkinsons_model.predict([[float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB), float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2), float(D2), float(PPE)]])
            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
        except ValueError:
            parkinsons_diagnosis = 'Please enter valid numeric values'
            
    st.success(parkinsons_diagnosis)


# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction Using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        patient_id = st.text_input('Enter your patient_ID')
    with col2:
        radius_mean = st.text_input('Radius mean value')
    with col3:
        texture_mean = st.text_input('Texture mean value')
    with col1:
        perimeter_mean = st.text_input('Perimeter mean value')
    with col2:
        area_mean = st.text_input('Area mean Level')
    with col3:
        smoothness_mean = st.text_input('Smoothness mean value')
    with col1:
        compactness_mean = st.text_input('Compactness mean value')
    with col2:
        concavity_mean = st.text_input('Concavity mean value')
    with col3:
        concave_points_mean = st.text_input('Concave points mean value')
    with col1:
        symmetry_mean = st.text_input('Symmetry mean value')
    with col2:
        fractal_dimension_mean = st.text_input('Fractal dimension mean value')
    with col3:
        radius_se = st.text_input('Radius SE value')
    with col1:
        texture_se = st.text_input('Texture SE value')
    with col2:
        perimeter_se = st.text_input('Perimeter SE value')
    with col3:
        area_se = st.text_input('Area SE value')
    with col1:
        smoothness_se = st.text_input('Smoothness SE value')
    with col2:
        compactness_se = st.text_input('Compactness SE value')
    with col3:
        concavity_se = st.text_input('Concavity SE value')
    with col1:
        concave_points_se = st.text_input('Concave points SE value')
    with col2:
        symmetry_se = st.text_input('Symmetry SE value')
    with col3:
        fractal_dimension_se = st.text_input('Fractal dimension SE value')
    with col1:
        radius_worst = st.text_input('Radius worst value')
    with col2:
        texture_worst = st.text_input('Texture worst value')
    with col3:
        perimeter_worst = st.text_input('Perimeter worst value')
    with col1:
        area_worst = st.text_input('Area worst value')
    with col2:
        smoothness_worst = st.text_input('Smoothness worst value')
    with col3:
        compactness_worst = st.text_input('Compactness worst value')
    with col1:
        concavity_worst = st.text_input('Concavity worst value')
    with col2:
        concave_points_worst = st.text_input('Concave points worst value')
    with col3:
        symmetry_worst = st.text_input('Symmetry worst value')
    with col1:
        fractal_dimension_worst = st.text_input('Fractal dimension worst value')

    breast_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Breast Cancer Test Result'):
        try:
            input_data = [
                float(patient_id), float(radius_mean), float(texture_mean), float(perimeter_mean), float(area_mean),
                float(smoothness_mean), float(compactness_mean), float(concavity_mean), float(concave_points_mean),
                float(symmetry_mean), float(fractal_dimension_mean), float(radius_se), float(texture_se),
                float(perimeter_se), float(area_se), float(smoothness_se), float(compactness_se), float(concavity_se),
                float(concave_points_se), float(symmetry_se), float(fractal_dimension_se), float(radius_worst),
                float(texture_worst), float(perimeter_worst), float(area_worst), float(smoothness_worst),
                float(compactness_worst), float(concavity_worst), float(concave_points_worst), float(symmetry_worst),
                float(fractal_dimension_worst)
            ]

            breast_cancer_prediction = breast_model.predict([input_data])
            if breast_cancer_prediction[0] == 1:
                breast_diagnosis = 'The Breast Cancer is Malignant'
            else:
                breast_diagnosis = 'The Breast Cancer is Benign'
        except ValueError:
            breast_diagnosis = 'Please enter valid numeric values'

    st.success(breast_diagnosis)