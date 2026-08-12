import streamlit as st
from datetime import datetime

CURRENT_YEAR = datetime.now().year #Current Year
CURRENT_DATE = datetime.now().strftime("%B %d, %Y") #Current Date

st.title("Phantaris :rainbow[𖤍]") #App name/main title

st.caption("Phantaris is not human. It may make mistakes")

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
