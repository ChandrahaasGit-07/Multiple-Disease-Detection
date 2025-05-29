import streamlit as st
import pandas as pd
import pickle
# import plotly.graph_objects as go
import numpy as np
from sklearn.preprocessing import StandardScaler
from streamlit_option_menu import option_menu
import os

# from streamlit_lottie import st_lottie_spinner
import streamlit.components.v1 as com  # used for adding a annimation to our app


st.set_page_config(
        page_title='Breast Cancer Diagnosis',
        page_icon='👩‍⚕️',
        layout='wide',
        initial_sidebar_state="expanded"
)

# Add background color using CSS
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #f0f8ff;  /* Light blue background */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background-color: #f0f8ff; /* Light blue */
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #f0f8ff; 
    }

    /* Navbar area (top of sidebar) */
    header[data-testid="stHeader"] {
        background-color: #f0f8ff;  
    }

    /* Brighten input boxes */
    input[type="text"], input[type="number"] {
        background-color: rgba(255, 255, 255, 0.9); 
     }

     /* Make all text black on all devices */
    body, .css-10trblm, .css-1d391kg, .stText, p, h1, h2, h3, h4, h5, h6, span, div {
        color: #333333 !important;
    }

    /* Target Streamlit primary buttons on mobile */
    @media (max-width: 767px) {
        /* Streamlit buttons inside div with role="button" */
        div.stButton > button {
            background-color: #ffffff !important;  /* light white/gray */
            color: #000000 !important;             /* black text */
            border: 1px solid #ccc !important;    /* subtle border */
            box-shadow: none !important;           /* remove shadow */
        }
    }

    /* Optional: Make text easier to read */
    .css-10trblm, .css-1d391kg {
        color: #f0f8ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# loading the save models 

file_path = os.path.join(os.path.dirname(__file__), 'saved_models', 'diabetes.pkl')
file_path2 = os.path.join(os.path.dirname(__file__), 'saved_models', 'heart.pkl')


with open(file_path,'rb')as file:
    diabetes_model = pickle.load(file)

with open(file_path2,'rb') as file:
    heart_model = pickle.load(file)


# sidebar for navigate
with st.sidebar:
    selected = option_menu('Main Menu',
                           ['Home',
                            'Diabetes Prediction',
                            'Heart Disease Prediction'],
                            menu_icon = 'hospital-fill',
                            icons=['house', 'activity', 'heart'],  # icons can be taken from BootStarp
                              default_index = 0)   # default_index = 0 means : we are selecting the first page which is "Diabetes Prediction Page"
    
    com.iframe('https://lottie.host/embed/652e04ed-343b-4cb3-9ce8-b55da65102ee/pwpx5ClYHq.lottie',height=200) 



# creating 2 columns
left_col, right_col = st.columns([3, 1])  #[3,1] indicates the size of left_column and right_column. '3'-->left_colummn takes 3 parts. '1'-->right_column 1 part

with left_col:

        # Home page
        if (selected == 'Home'):
                st.image('image1.png')
                st.title("Welcome to the Health Prediction Web App!")
                st.markdown(
                        '''
                                This app helps you find out your risk of having certain diseases based on the information you provide.  
                                Using trained machine learning models, we offer predictions for:

                                - **Diabetes**
                                - **Heart Disease**
                                - **Lung Cancer**

                                Just enter your health details, and the app will do the rest!
                        '''
                )


                # Assigining the images on "Home Page"
                col1, col2 = st.columns(2)   # defining 2 columns in "Home Page" to assign 2 images side-by-side
                with col1:
                        st.image("https://img.freepik.com/premium-vector/doctors-testing-blood-glucose-using-glucometer-hypoglycemia-diabetes-diagnosis-laboratory-equipment-syringe-physician-measuring-sugar-level_284092-2708.jpg", width=250, caption="Diabetes Prediction")

                with col2:
                        st.image('https://www.heart.org/-/media/Images/Around-the-AHA/2022-Top-10_SC.jpg', width=200, caption="Heart Disease")

                st.title('How to Use:')
                st.markdown(
                        '''
                        - Navigate to the Main Menu(>) located in the top-left corner of the screen.
                        - Click on the desired tab among 'Diabetes Prediction', 'Heart Disease' to access prediction tools for specific diseases.
                        - Enter relevant information as requested in the input fields.
                        - Click on the "Test Result" button to obtain predictions based on the provided data.
                        '''
                )

                st.title('Disclaimer:')
                st.markdown(
                        '''
                        - This Web App may not provide accurate predictions at all times. When in doubt, please enter the values again and verify the predictions.
                        - It is important to note that individuals with specific risk factors or concerns should consult with healthcare professionals for personalized advice and management.
                        '''
                )

        # Diabetes prediction page
        if (selected=='Diabetes Prediction'):
        
                st.title('Diabetes Prediction Page')

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


                # code for Prediction
                diab_diagnosis = ''

                # creating a button for Prediction

                if st.button('Diabetes Test Result'):

                        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                                BMI, DiabetesPedigreeFunction, Age]

                        user_input = [float(x) for x in user_input] # Converts each x into a float using float(x) 

                        diab_prediction = diabetes_model.predict([user_input])

                        if diab_prediction[0] == 1:
                                diab_diagnosis = 'The person is diabetic'
                        else:
                                diab_diagnosis = 'The person is not diabetic'
                else:
                        st.text('Please provide input')
                
                if diab_diagnosis == 'The person is not diabetic':
                        st.success(diab_diagnosis)
                        com.iframe('https://lottie.host/embed/06e5989e-3266-40d2-bdbc-7be5ba8ffca3/viojdUZWIs.lottie')
                else:
                        st.success(diab_diagnosis)

        #     st.title('Diabetes Prediction Page')
        
        #     Pregnancies = st.text_input('Number of Pregnancies')
        #     Glucose = st.text_input('Glucose level')
        #     BloodPressure = st.text_input('BloodPressure value')
        #     SkinThickness = st.text_input('SkinThickness value')
        #     Insulin = st.text_input('Insulin value')
        #     BMI = st.text_input('BMI number')
        #     DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction number')
        #     Age = st.text_input('Age of person')

        # # code for prediction ( end result )
        #     diab_diagnosis = ''

        #     if st.button('Diabetes Test Result'):

        #         diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])   # predict with respect to this input values, and input values are consider as a 2D array
                
        #         # user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
        #         #               BMI, DiabetesPedigreeFunction, Age]

        #         # diab_prediction = diabetes_model.predict([user_input])

        #         if diab_prediction[0] == 1:
        #             diab_diagnosis = 'The person is diabetic'
        #         else:
        #             diab_diagnosis = 'The person is not diabetic'

        #     st.success(diab_diagnosis)




        if (selected == 'Heart Disease Prediction'):
        
                # com.iframe('https://lottie.host/embed/6fcf059e-9373-4a81-a9e8-30f9f96aacdd/xP8vbRv68X.lottie')

                st.title('Heart Disease Prediction Page')

                col1, col2, col3 = st.columns(3)

                with col1:
                        age = st.text_input('Age')

                with col2:
                        sex = st.text_input('Sex -> 1 : Male, 2 : Female')

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

                # code for Prediction
                heart_diagnosis = ''

                # creating a button for Prediction

                if st.button('Heart Disease Test Result'):

                        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

                        user_input = [float(x) for x in user_input]

                        heart_prediction = heart_model.predict([user_input])  # this line defines : it takes the input and gives to "heart_model"(model which is created) for prediction

                        if heart_prediction[0] == 1:
                                heart_diagnosis = 'The person is having heart disease'
                        else:
                                heart_diagnosis = 'The person does not have any heart disease'
                else:
                        st.text('Please provide the input')

                if heart_diagnosis == 'The person does not have any heart disease':
                        st.success(heart_diagnosis)
                        com.iframe('https://lottie.host/embed/97d781b8-c24e-47ae-952a-35a47ffda162/RgikOoDHZd.lottie')
                else:
                        st.success(heart_diagnosis)
                        # com.iframe('https://lottie.host/embed/02641387-7044-414f-9a82-a2aae30b1d5f/JuiN3bqeUZ.lottie')


# right_column
with right_col:
        if (selected == 'Heart Disease Prediction'):
                com.iframe('https://lottie.host/embed/6fcf059e-9373-4a81-a9e8-30f9f96aacdd/xP8vbRv68X.lottie')
        
        if (selected == 'Diabetes Prediction'):
                com.iframe('https://lottie.host/embed/df070cfe-46f0-4450-9313-a540f7e489d3/GcVNhMM8kx.lottie')
