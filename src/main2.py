import streamlit as st
import os
import json
from PyPDF2 import PdfReader  # Import PdfReader instead of PdfFileReader


# Initialize the session state
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Rule-based response
def get_bot_response(user_input):
    rules = {
        "hello": "Hi there!",
        "how are you?": "I'm a chatbot, so I'm always good.",
        "bye": "Goodbye!",
        "save uploaded pdf": save_uploaded_pdf,  # Correctly reference the function
        "show text": extract_text_from_pdf,
        "generate embeding": __name__
    }
    return rules.get(user_input.lower(), "I don't understand that. Can you rephrase?")

def save_uploaded_pdf():
    uploaded_files = st.session_state.get('uploaded_files', [])  # Retrieve uploaded files from session state
    
    if not uploaded_files:
        st.sidebar.warning("Please upload PDF files first.")
        return
    
    if not os.path.exists("extracted_texts"):
        os.makedirs("extracted_texts")  # Create directory if it doesn't exist
    
    for file in uploaded_files:
        file_name = file.name
        file_path = os.path.join("extracted_texts", file_name)
        
        # Save the uploaded PDF file
        with open(file_path, 'wb') as f:
            f.write(file.read())
        
        # Extract text from PDF using your preferred method
        extracted_text = extract_text_from_pdf(file_path)  # Replace with your text extraction logic
        
        # Save as .txt
        with open(os.path.join("extracted_texts", f"{file_name}.txt"), 'w', encoding='utf-8') as f:
            f.write(extracted_text)
        
        # Save as .json (optional if you need to store additional metadata)
        with open(os.path.join("extracted_texts", f"{file_name}.json"), 'w', encoding='utf-8') as f:
            json.dump({"file_name": file_name, "extracted_text": extracted_text}, f, indent=4)

def extract_text_from_pdf(file_path):
    # Example using PdfReader from PyPDF2 to extract text from PDF
    text = ''
    with open(file_path, 'rb') as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to handle user input
def handle_user_input():
    user_input = st.session_state['user_input']
    if user_input:
        st.session_state['messages'].append({"user": user_input, "bot": get_bot_response(user_input)})
        if user_input.lower() == "save uploaded pdf":
            save_uploaded_pdf()  # Call save_uploaded_pdf function
        st.session_state['user_input'] = ''  # Clear input field

# Attach files
uploaded_files = st.sidebar.file_uploader("Attach files", accept_multiple_files=True, key="file_uploader")
st.session_state['uploaded_files'] = uploaded_files  # Store uploaded files in session state

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



#----------------generate embedings---------------------
from generate_embedings import load_model, read_text_from_file, generate_embeddings, save_embeddings

if __name__ == "__main__":
    # Load the model
    model = load_model()

    # Directory containing extracted text files
    input_dir = "extracted_texts"
    output_dir = "embeddings"
    os.makedirs(output_dir, exist_ok=True)

    # Process each text file and generate embeddings
    for text_file in os.listdir(input_dir):
        if text_file.endswith(".txt"):
            text_path = os.path.join(input_dir, text_file)
            text = read_text_from_file(text_path)
            embeddings = generate_embeddings(model, [text])  # Generate embeddings for the text

            # Save embeddings
            embedding_file = os.path.splitext(text_file)[0] + ".npy"
            output_path = os.path.join(output_dir, embedding_file)
            save_embeddings(embeddings, output_path)
            print(f"Saved embeddings to {output_path}")
