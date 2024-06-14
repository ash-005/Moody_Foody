from dotenv import load_dotenv
load_dotenv() ## Loading environment variables
import streamlit as st
import os
import google.generativeai as genai
import time

genai.configure(api_key=os.getenv('GOOGLE_API_KEY')) ## Configuring  API key
## function to load Gemini Pro
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(mood):
    # prompt = '''
    #                     Prompt: 
    #                     Your tone should be friendly. You will receive either some type of food item in which case give the recipe for that dish. If it is any cuisine suggest some dishes from that cuisine. 
    #                     User can also give their mood, and emotions based on which you can suggest some food.
    #                     You are to give five food recommendations based on users mood. Make sure that you do not give any more recommendations for other moods other than mentioned by the user.
    #                      Make sure that the dishes are vegetarian and based on vegetarian food make it related to indian cuisine.
    #                     The input will be of type "this definition + Mood: user_mood " 
    #                     '''
    prompt = '''You are a Food recommendor. You get users mood and suggest them dishes based on their mood. Make sure that the dishes are vegeterian and
    also make sure that you suggest dishes from Indian cusine and chinense and other cusines where they have vegetarian dishes.
    You can give total of five recommendations to the user based on their mood. Also give some remarks like "Oh you are feeling [their mood] here are few dishes you can try out based on your mood".
    
    User can give input as "I am feeling happy" or "I am feeling bored" or just "Happy" or "Sad" so based on that give your recommendations to their mood.
'''
    #recom = prompt + "Mood: " + str(mood)
    recom = prompt + str(mood)
    response = model.generate_content(recom)
    return response.text


## setting up streamlit app
st.set_page_config(page_title='Moody Foody')
st.header('AI-Ded Dish Recommendations')
st.title('Moody Foody Recommendations')
st.markdown('Discover delicious vegetarian dishes tailored to your mood with our AI-powered food recommender.')

## Input method for user interaction
input_method = st.radio('Choose input method:', ['Enter mood manually', 'Select from dropdown'])

if input_method == 'Enter mood manually':
    mood: str = st.text_input("Mood: ", key="mood")
else:
    moods = ['Happy', 'Sad', 'Bored', 'Stressed', 'Anxious', 'Energetic', 'Tired', 'Excited', 'Calm']
    mood = st.selectbox('Mood:', moods)
submit: bool = st.button("Submit")
import pandas as pd

if submit:
    response = get_gemini_response(mood)
    dishes = response.split('\n')
    df = pd.DataFrame(dishes, columns=['Dishes'])
    st.table(df)

clear_selection = st.button('Clear Selection')
if clear_selection:
    mood = ''



st.markdown('---')
st.markdown('Contact us: [loginsbaggins@gmail.com](mailto:loginsbaggins@gmail.com)')

# mood: str = st.text_input("Mood: ",key="mood")
# submit: bool = st.button("Submit")
# if submit:
#     response = get_gemini_response(mood)
#     st.write(response)
# st.markdown('---')
# st.markdown('Contact us: [loginsbaggins@gmail.com](mailto:loginsbaggins@gmail.com)')

