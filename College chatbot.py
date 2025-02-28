import streamlit as st
import pandas as pd
import google.generativeai as genai
form sklearn.metrics.paiwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

st.set_page_config(page_title="SVECW College Chatbot",layout="centered")
if "messages" not in st.session_state:
  st.session_state.messages=[]
csv_url="svecw_details chatbot.csv"
try:
  df=pd.read_csv(csv_url)
except Eception as e:
  st.error(f'failed to load the CSV file. Error:{e}")
  st.stop()
df=df.fillna("")
df['Question']=df['Question'].str.lower()
df['Answer']=df['Answer'].str.lower()


vectorizer=TfidfVectorizer()
question_vectors=vectorizer.fit_transform(df['Question'])
API_KEY="

