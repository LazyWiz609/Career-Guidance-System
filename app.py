# import streamlit as st
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder
# import joblib
# le = LabelEncoder()
# # Load your trained model (assuming you've saved it)
# model = joblib.load('trained_model.joblib')

# st.title('Career Guidance System')

# st.write('Please answer the following questions to receive career recommendations.')

# # Create input fields for user data
# education = st.selectbox('What is your highest level of education?', ['High School', "Bachelor's", "Master's", 'PhD'])
# academic_interest = st.text_input('What are your main areas of academic interest?')
# problem_solving = st.slider('How would you rate your problem-solving skills on a scale of 1-10?', 1, 10)
# communication = st.slider('How would you rate your communication skills on a scale of 1-10?', 1, 10)
# tech_comfort = st.slider('How comfortable are you with using technology? (1-10)', 1, 10)
# work_preference = st.radio('Do you prefer working independently or in a team?', ['Independent', 'Team'])
# interests = st.text_input('What are your top 3 personal interests or hobbies?')
# work_life_balance = st.slider('How important is work-life balance to you on a scale of 1-10?', 1, 10)
# further_education = st.radio('Are you willing to pursue further education or training for your career?', ['Yes', 'No'])
# work_environment = st.radio('Do you prefer a stable work environment or one that involves frequent changes?', ['Stable', 'Dynamic'])
# leadership = st.slider('How would you rate your leadership skills on a scale of 1-10?', 1, 10)
# data_interest = st.radio('Are you interested in working with data and analytics?', ['Yes', 'No'])
# public_speaking = st.slider('How comfortable are you with public speaking? (1-10)', 1, 10)
# task_preference = st.radio('Do you enjoy creative tasks or more structured, analytical work?', ['Creative', 'Analytical'])
# salary_expectation = st.selectbox('What salary range are you aiming for in your future career?', ['Entry-level', 'Mid-range', 'High-end'])

# # Fit LabelEncoder with categorical variables
# categorical_vars = ['education', 'work_preference', 'further_education', 'work_environment', 'data_interest', 'task_preference', 'salary_expectation']
# for var in categorical_vars:
#     le.fit(pd.read_csv('preprocessed_data.csv')[var].unique())

# def predict_career(user_input):
#     # Preprocess user input to match your model's expected format
#     # Example (adjust based on your actual preprocessing steps):
#     processed_input = []
#     for i, value in enumerate(user_input):
#         if isinstance(value, str):
#             # Encode categorical variables
#             processed_input.append(le.transform([value])[0])
#         else:
#             # Scale numerical features if necessary
#             processed_input.append(value)
    
#     # Make prediction using your trained model
#     prediction = model.predict([processed_input])
#     return prediction[0]

# if st.button('Get Career Recommendation'):
#     user_input = [education, academic_interest, problem_solving, communication, tech_comfort, work_preference, 
#                   interests, work_life_balance, further_education, work_environment, leadership, data_interest, 
#                   public_speaking, task_preference, salary_expectation]
#     career_recommendation = predict_career(user_input)
#     st.write(f"Based on your inputs, we recommend exploring careers in: {career_recommendation}")

# import streamlit as st
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder
# import joblib

# # Load your trained model
# model = joblib.load('trained_model.joblib')

# # Load the preprocessed data
# df = pd.read_csv('preprocessed_data.csv')

# # Initialize LabelEncoder and fit it with categorical variables
# le = LabelEncoder()
# categorical_vars = ['preferredLabel_en', 'preferredLabel_de']
# for var in categorical_vars:
#     le.fit(df[var].unique())

# st.title('Career Guidance System')

# st.write('Please answer the following questions to receive career recommendations.')

# # Create input fields for user data
# experience_order = st.slider('How many years of experience do you have?', 0, 10)
# preferred_label_en = st.text_input('What is your preferred job title in English?')
# preferred_label_de = st.text_input('What is your preferred job title in German?')

# # Additional questions (these won't be used in prediction but can be used for future enhancements)
# education = st.selectbox('What is your highest level of education?', ['High School', "Bachelor's", "Master's", 'PhD'])
# academic_interest = st.text_input('What are your main areas of academic interest?')
# problem_solving = st.slider('How would you rate your problem-solving skills on a scale of 1-10?', 1, 10)
# communication = st.slider('How would you rate your communication skills on a scale of 1-10?', 1, 10)
# tech_comfort = st.slider('How comfortable are you with using technology? (1-10)', 1, 10)
# work_preference = st.radio('Do you prefer working independently or in a team?', ['Independent', 'Team'])
# interests = st.text_input('What are your top 3 personal interests or hobbies?')
# work_life_balance = st.slider('How important is work-life balance to you on a scale of 1-10?', 1, 10)
# further_education = st.radio('Are you willing to pursue further education or training for your career?', ['Yes', 'No'])
# work_environment = st.radio('Do you prefer a stable work environment or one that involves frequent changes?', ['Stable', 'Dynamic'])
# leadership = st.slider('How would you rate your leadership skills on a scale of 1-10?', 1, 10)
# data_interest = st.radio('Are you interested in working with data and analytics?', ['Yes', 'No'])
# public_speaking = st.slider('How comfortable are you with public speaking? (1-10)', 1, 10)
# task_preference = st.radio('Do you enjoy creative tasks or more structured, analytical work?', ['Creative', 'Analytical'])
# salary_expectation = st.selectbox('What salary range are you aiming for in your future career?', ['Entry-level', 'Mid-range', 'High-end'])

# def predict_career(user_input):
#     processed_input = []
#     for value in user_input:
#         if isinstance(value, str):
#             try:
#                 processed_input.append(le.transform([value])[0])
#             except ValueError:
#                 # Assign a default value for unknown labels
#                 processed_input.append(-1)
#         else:
#             processed_input.append(value)
    
#     prediction = model.predict([processed_input])
#     return prediction[0]

# if st.button('Get Career Recommendation'):
#     user_input = [experience_order, preferred_label_en, preferred_label_de]
    
#     career_recommendation = predict_career(user_input)
#     st.write(f"Based on your inputs, we recommend exploring careers in: {career_recommendation}")

# st.write("Note: This is a prototype demonstration. In a full implementation, all input fields would be used for a more comprehensive career recommendation.")

# import streamlit as st
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder
# import joblib

# # Load your trained model
# model = joblib.load('trained_model.joblib')

# # Load the preprocessed data
# df = pd.read_csv('preprocessed_data.csv')

# # Initialize LabelEncoder and fit it with categorical variables
# le = LabelEncoder()
# categorical_vars = ['preferredLabel_en', 'preferredLabel_de']
# for var in categorical_vars:
#     le.fit(df[var].unique())

# st.title('Career Guidance System')

# st.write('Please answer the following questions to receive career recommendations.')

# # Create input fields for user data
# _id = st.number_input('Enter ID', min_value=0)
# experience_order = st.slider('How many years of experience do you have?', 0, 10)
# valid_job_titles = df['preferredLabel_en'].unique().tolist()
# preferred_label_en = st.selectbox('What is your preferred job title in English?', valid_job_titles)
# preferred_label_de = st.selectbox('What is your preferred job title in German?', df['preferredLabel_de'].unique().tolist())

# # Additional questions for future enhancements
# st.subheader('Additional Information (Not used for current prediction)')
# education = st.selectbox('What is your highest level of education?', ['High School', "Bachelor's", "Master's", 'PhD'])
# academic_interest = st.text_input('What are your main areas of academic interest?')
# problem_solving = st.slider('How would you rate your problem-solving skills on a scale of 1-10?', 1, 10)
# communication = st.slider('How would you rate your communication skills on a scale of 1-10?', 1, 10)
# tech_comfort = st.slider('How comfortable are you with using technology? (1-10)', 1, 10)
# work_preference = st.radio('Do you prefer working independently or in a team?', ['Independent', 'Team'])
# interests = st.text_input('What are your top 3 personal interests or hobbies?')
# work_life_balance = st.slider('How important is work-life balance to you on a scale of 1-10?', 1, 10)
# further_education = st.radio('Are you willing to pursue further education or training for your career?', ['Yes', 'No'])
# work_environment = st.radio('Do you prefer a stable work environment or one that involves frequent changes?', ['Stable', 'Dynamic'])
# leadership = st.slider('How would you rate your leadership skills on a scale of 1-10?', 1, 10)
# data_interest = st.radio('Are you interested in working with data and analytics?', ['Yes', 'No'])
# public_speaking = st.slider('How comfortable are you with public speaking? (1-10)', 1, 10)
# task_preference = st.radio('Do you enjoy creative tasks or more structured, analytical work?', ['Creative', 'Analytical'])
# salary_expectation = st.selectbox('What salary range are you aiming for in your future career?', ['Entry-level', 'Mid-range', 'High-end'])

# def predict_career(user_input):
#     processed_input = []
#     for i, value in enumerate(user_input):
#         if i == 0:  # _id
#             processed_input.append(value)
#         elif i == 1:  # experience_order
#             processed_input.append(value)
#         elif i == 2 or i == 3:  # preferredLabel_en and preferredLabel_de
#             if value in le.classes_:
#                 processed_input.append(le.transform([value])[0])
#             else:
#                 processed_input.append(-1)  # Use a default value for unknown labels
    
#     if len(processed_input) != 4:
#         raise ValueError(f"Expected 4 features, but got {len(processed_input)}")
    
#     prediction = model.predict([processed_input])
#     return prediction[0]

# if st.button('Get Career Recommendation'):
#     user_input = [_id, experience_order, preferred_label_en, preferred_label_de]
    
#     try:
#         career_recommendation = predict_career(user_input)
#         st.success(f"Based on your inputs, we recommend exploring careers in: {career_recommendation}")
        
#         # Display additional information about the recommended career
#         career_info = df[df['preferredLabel_en'] == career_recommendation].iloc[0]
#         st.write(f"Description: {career_info['description_en']}")
#         st.write("Key skills:")
#         for skill in eval(career_info['skills']):
#             st.write(f"- {skill}")
#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}. Please try again with different inputs.")

# st.info("Note: This is a prototype demonstration. In a full implementation, all input fields would be used for a more comprehensive career recommendation.")

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load your trained model
model = joblib.load('trained_model.joblib')

# Load the preprocessed data
df = pd.read_csv('preprocessed_data.csv')

# Initialize LabelEncoder and fit it with categorical variables
le = LabelEncoder()
categorical_vars = ['preferredLabel_en']
for var in categorical_vars:
    le.fit(df[var].unique())

st.title('Career Guidance System')

st.write('Please answer the following questions to receive career recommendations.')

# Create input fields for user data
experience_order = st.slider('How many years of experience do you have?', 0, 10)
valid_job_titles = df['preferredLabel_en'].unique().tolist()
preferred_label_en = st.selectbox('What is your preferred job title in English?', valid_job_titles)

# Additional questions for future enhancements
st.subheader('Additional Information (Not used for current prediction)')
education = st.selectbox('What is your highest level of education?', ['High School', "Bachelor's", "Master's", 'PhD'])
academic_interest = st.text_input('What are your main areas of academic interest?')
problem_solving = st.slider('How would you rate your problem-solving skills on a scale of 1-10?', 1, 10)
communication = st.slider('How would you rate your communication skills on a scale of 1-10?', 1, 10)
tech_comfort = st.slider('How comfortable are you with using technology? (1-10)', 1, 10)
work_preference = st.radio('Do you prefer working independently or in a team?', ['Independent', 'Team'])
interests = st.text_input('What are your top 3 personal interests or hobbies?')
work_life_balance = st.slider('How important is work-life balance to you on a scale of 1-10?', 1, 10)
further_education = st.radio('Are you willing to pursue further education or training for your career?', ['Yes', 'No'])
work_environment = st.radio('Do you prefer a stable work environment or one that involves frequent changes?', ['Stable', 'Dynamic'])
leadership = st.slider('How would you rate your leadership skills on a scale of 1-10?', 1, 10)
data_interest = st.radio('Are you interested in working with data and analytics?', ['Yes', 'No'])
public_speaking = st.slider('How comfortable are you with public speaking? (1-10)', 1, 10)
task_preference = st.radio('Do you enjoy creative tasks or more structured, analytical work?', ['Creative', 'Analytical'])
salary_expectation = st.selectbox('What salary range are you aiming for in your future career?', ['Entry-level', 'Mid-range', 'High-end'])

def predict_career(user_input):
    processed_input = []
    for i, value in enumerate(user_input):
        if i == 0:  # experience_order
            processed_input.append(value)
        elif i == 1 or i == 2:  # preferredLabel_en and preferredLabel_de
            if value in le.classes_:
                processed_input.append(le.transform([value])[0])
            else:
                processed_input.append(-1)  # Use a default value for unknown labels
    
    if len(processed_input) != 2:
        raise ValueError(f"Expected 3 features, but got {len(processed_input)}")
    
    prediction = model.predict([processed_input])
    return prediction[0]

if st.button('Get Career Recommendation'):
    user_input = [experience_order, preferred_label_en]
    
    try:
        career_recommendation = predict_career(user_input)
        st.success(f"Based on your inputs, we recommend exploring careers in: {career_recommendation}")
        
        # Display additional information about the recommended career
        career_info = df[df['preferredLabel_en'] == career_recommendation].iloc[0]
        st.write(f"Description: {career_info['description_en']}")
        st.write("Key skills:")
        for skill in eval(career_info['skills']):
            st.write(f"- {skill}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}. Please try again with different inputs.")

st.info("Note: This is a prototype demonstration. In a full implementation, all input fields would be used for a more comprehensive career recommendation.")
