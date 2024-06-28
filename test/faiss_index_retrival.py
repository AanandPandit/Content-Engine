import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def load_model(model_name='paraphrase-MiniLM-L6-v2'):
    """Load the SentenceTransformer model."""
    model = SentenceTransformer(model_name)
    return model

def generate_embeddings(model, texts):
    """Generate embeddings for a list of texts using the model."""
    embeddings = model.encode(texts, convert_to_tensor=False)
    return embeddings

def create_faiss_index(embedding_dim):
    """Create a Faiss index for storing embeddings."""
    index = faiss.IndexFlatL2(embedding_dim)  # L2 distance index
    return index

def add_embeddings_to_index(index, embeddings):
    """Add embeddings to the Faiss index."""
    index.add(embeddings)

def save_faiss_index(index, index_path):
    """Save the Faiss index to a file."""
    faiss.write_index(index, index_path)

def load_faiss_index(index_path):
    """Load the Faiss index from a file."""
    index = faiss.read_index(index_path)
    return index

def search_similar_embeddings(index, query_embeddings, k=5):
    """Search for the top k similar embeddings."""
    distances, indices = index.search(query_embeddings, k)
    return distances, indices

def test_vector_storage():
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

    # Convert embeddings to numpy array
    embeddings = np.array(embeddings).astype('float32')

    # Create a Faiss index
    embedding_dim = embeddings.shape[1]
    index = create_faiss_index(embedding_dim)

    # Add embeddings to the Faiss index
    add_embeddings_to_index(index, embeddings)

    # Save the Faiss index to a file
    index_path = "embeddings.index"
    save_faiss_index(index, index_path)
    print(f"Faiss index saved to {index_path}")

    # Load the Faiss index from the file
    loaded_index = load_faiss_index(index_path)

    # Example query
    query_texts = ["Electric vehicles and renewable energy."]
    query_embeddings = generate_embeddings(model, query_texts)
    query_embeddings = np.array(query_embeddings).astype('float32')

    # Search for similar embeddings
    distances, indices = search_similar_embeddings(loaded_index, query_embeddings)
    print("Top similar embeddings indices:", indices)
    print("Top similar embeddings distances:", distances)

    # Verify the results
    for idx in indices[0]:
        print(f"Text: {sample_texts[idx]}")

if __name__ == "__main__":
    test_vector_storage()
