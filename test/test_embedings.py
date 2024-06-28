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

def save_embeddings(embeddings, output_path):
    """Save embeddings to a file."""
    np.save(output_path, embeddings)

if __name__ == "__main__":
    # Load the model
    model = load_model()

    # Define sample texts
    sample_texts = [
        "Alphabet Inc. is a multinational conglomerate.",
        "Tesla, Inc. specializes in electric vehicles.",
        "Uber Technologies, Inc. is a ride-sharing company."
    ]

    # Generate embeddings for the sample texts
    embeddings = generate_embeddings(model, sample_texts)

    # Save the embeddings to a file
    output_path = "sample_embeddings.npy"
    save_embeddings(embeddings, output_path)
    print(f"Saved embeddings to {output_path}")

    # Load the embeddings back to verify
    loaded_embeddings = np.load(output_path)
    print("Loaded embeddings:", loaded_embeddings)
