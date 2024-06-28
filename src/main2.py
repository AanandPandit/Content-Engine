import streamlit as st
import fitz  # PyMuPDF
import os
import json

# Initialize the session state
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Function to extract text from PDF file object
def extract_text_from_pdf(uploaded_file):
    pdf_data = uploaded_file.read()  # Read the file content
    document = fitz.open(stream=pdf_data, filetype="pdf")
    text = ""

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    return text

# Function to save text to file
def save_text_to_file(text, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

# Function to save texts to JSON
def save_texts_to_json(texts, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(texts, file, ensure_ascii=False, indent=4)

# Attach files
uploaded_files = st.sidebar.file_uploader("Attach files", accept_multiple_files=True, key="file_uploader")

# Display uploaded files and extract text
if uploaded_files:
    st.sidebar.write("### Attached Files:")
    for uploaded_file in uploaded_files:
        st.sidebar.write(f"- {uploaded_file.name}")

        # Extract text from PDF file
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
            st.sidebar.write(f"#### Extracted Text from {uploaded_file.name}:")
            st.sidebar.write(text)

            # Save extracted text to a file in the working directory
            filename = os.path.splitext(uploaded_file.name)[0]
            output_path_txt = os.path.join("extracted_texts", filename + ".txt")
            save_text_to_file(text, output_path_txt)
            st.sidebar.write(f"Saved extracted text to: `{output_path_txt}`")

# Main content: Chatbot and chat history
st.write("# Chatbot")

# Chat history
for idx, message in enumerate(st.session_state['messages']):
    st.write(f"**You:** {message['user']}")
    st.write(f"**Bot:** {message['bot']}")

# Fixed user input field at the bottom
st.sidebar.text_input("Type your message here", key="user_input")

# Send button
def handle_user_input():
    user_input = st.sidebar.session_state['user_input']
    if user_input:
        st.session_state['messages'].append({"user": user_input, "bot": "Chatbot response placeholder"})
        st.sidebar.session_state['user_input'] = ''  # Clear input field

st.sidebar.button("Send", on_click=handle_user_input, key="send_button")
