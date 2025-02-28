import streamlit as st
import pandas as pd
import google.generativeai as genai
form sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

st.set_page_config(page_title="SVECW College Chatbot",layout="centered")
if "messages" not in st.session_state:
  st.session_state.messages=[]
csv_url="svecw_details chatbot.csv"
try:
  df=pd.read_csv(csv_url)
except Exception as e:
  st.error(f"failed to load the CSV file. Error:{e}")
  st.stop()
df=df.fillna("")
df['Question']=df['Question'].str.lower()
df['Answer']=df['Answer'].str.lower()


vectorizer=TfidfVectorizer()
question_vectors=vectorizer.fit_transform(df['Question'])
API_KEY="AIzaSyDXIsk8yeqplDNzm2k514Qv2z9mgAKUdTk"
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel('gemini-1.5-flash')
def find_closest_question(user_query,vectorizer,question_vectors,df):
  query_vector=vectorizer.transform([user_query.lower()])
  similarities=cosine_similarity(query_vector,question_vectors).flatten()
  best_match_index=similarities.argmax()
  best_match_score=similarities[best_match_index]
  if best_match_score>0.3:
    return df.iloc[best_match_index]['Answer']
  else:
    return None
st.title("SVECW College CHatbot")
st.write("Welcome to the College Chatbot! Ask me anything about the College.")
 
