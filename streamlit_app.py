import streamlit as st
from streamlit_push_notifications import send_push
from datetime import datetime

CURRENT_YEAR = datetime.now().year #Current Year
CURRENT_DATE = datetime.now().strftime("%B %d, %Y") #Current Date

st.title("Phantaris :rainbow[𖤍]") #App name/main title

st.caption("Phantaris is not human. It may make mistakes")

st.title("Notification Demo")

if st.button("Trigger System Notification"):
    # This requests permission if not already granted, then sends the alert
    (
        send_push(title="Alert", body="Process finished")
    )

with st.sidebar:
    if st.button("Login"):
        st.write("Init Login")
        "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
        "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"


# Pill-shaped chat input
st.markdown("""
<style>
[data-testid="stChatInput"] {
    border-radius: 30px !important;
    overflow: hidden;
}
[data-testid="stChatInput"] textarea {
    border-radius: 30px !important;
}
[data-testid="stChatInputContainer"] {
    border-radius: 30px !important;
}
</style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask a question..."): #The text on the input bar
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    response = f"echo:{prompt}"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    #openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
