import streamlit as st
import google.generativeai as genai


st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖"
)

genai.configure(api_key=("API_KEY"))
model=genai.GenerativeModel("models/gemini-2.5-flash")

st.title("🌐 Personal AI Chatbot 🌐")  # change the name of chatbot from here
if "message" not in st.session_state:
    st.session_state.message=[]

for message in st.session_state.message:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt=st.chat_input("Type your message...")

if prompt:
    st.session_state.message.append(
        {
            "role":"user",
            "content":prompt
        }
    )
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("thinking..."):
            response=model.generate_content(prompt)
            ai_response=response.text

            st.write(ai_response)

            st.session_state.message.append({
                "role":"assistant",
                "content":ai_response})





