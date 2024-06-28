
import os
from sentence_transformers import SentenceTransformer
import numpy as np

def load_model(model_name='paraphrase-MiniLM-L6-v2'):
    """Load the SentenceTransformer model."""
    model = SentenceTransformer(model_name)
    return model

def generate_embeddings(model, texts):
    """Generate embeddings for a list of texts using the model."""
    embeddings = model.encode(texts, convert_to_tensor=False)
    return embeddings

def read_text_from_file(file_path):
    """Read the content of a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def save_embeddings(embeddings, output_path):
    """Save embeddings to a file."""
    np.save(output_path, embeddings)

# if __name__ == "__main__":
#     # Load the model
#     model = load_model()

#     # Directory containing extracted text files
#     input_dir = "extracted_texts"
#     output_dir = "embeddings"
#     os.makedirs(output_dir, exist_ok=True)

#     # Process each text file and generate embeddings
#     for text_file in os.listdir(input_dir):
#         if text_file.endswith(".txt"):
#             text_path = os.path.join(input_dir, text_file)
#             text = read_text_from_file(text_path)
#             embeddings = generate_embeddings(model, [text])  # Generate embeddings for the text

#             # Save embeddings
#             embedding_file = os.path.splitext(text_file)[0] + ".npy"
#             output_path = os.path.join(output_dir, embedding_file)
#             save_embeddings(embeddings, output_path)
#             print(f"Saved embeddings to {output_path}")
