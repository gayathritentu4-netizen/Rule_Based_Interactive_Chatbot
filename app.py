import streamlit as st
from chatbot import get_response

# Page configuration
st.set_page_config(
    page_title="Student Support Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Page title
st.title("🤖 Student Support Assistant")

st.write(
    "Welcome! Ask me about business hours, "
    "internship project submission, or certificates."
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Type your question here...")

if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Generate bot response
    response = get_response(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)

# Clear conversation button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()