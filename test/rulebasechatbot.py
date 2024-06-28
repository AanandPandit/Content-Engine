import streamlit as st

# Initialize the session state
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Rule-based response
def get_bot_response(user_input):
    rules = {
        "hello": "Hi there!",
        "how are you?": "I'm a chatbot, so I'm always good.",
        "bye": "Goodbye!"
    }
    return rules.get(user_input.lower(), "I don't understand that. Can you rephrase?")

# Function to handle user input
def handle_user_input():
    user_input = st.session_state['user_input']
    if user_input:
        st.session_state['messages'].append({"user": user_input, "bot": get_bot_response(user_input)})
        st.session_state['user_input'] = ''  # Clear input field

# Attach files
uploaded_files = st.sidebar.file_uploader("Attach files", accept_multiple_files=True, key="file_uploader")

# Display uploaded files (if any)
if uploaded_files:
    st.sidebar.write("### Attached Files:")
    for file in uploaded_files:
        st.sidebar.write(f"- {file.name}")

# Main content: Chatbot and chat history
st.write("# Chatbot")

# Chat history
for idx, message in enumerate(st.session_state['messages']):
    st.write(f"**You:** {message['user']}")
    st.write(f"**Bot:** {message['bot']}")

# Fixed user input field at the bottom
st.sidebar.text_input("Type your message here", key="user_input", on_change=handle_user_input)

# Send button
st.sidebar.button("Send", on_click=handle_user_input, key="send_button")
