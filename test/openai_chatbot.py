import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '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'

st.title("Streamlit Chatbot")

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model name, like "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        message = response.choices[0].message['content'].strip()
        return message
    except Exception as e:
        return f"Error: {e}"

# Display the chat messages
for msg in st.session_state['messages']:
    st.write(msg)

# User input
user_input = st.text_input("You: ", key="user_input")

if st.button("Send"):
    if user_input:
        st.session_state['messages'].append(f"You: {user_input}")
        response = generate_response(user_input)
        st.session_state['messages'].append(f"Chatbot: {response}")

# Display the chat messages
for msg in st.session_state['messages']:
    st.write(msg)
