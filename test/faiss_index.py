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

def search_similar_embeddings(index, query_embeddings, k=5):
    """Search for the top k similar embeddings."""
    distances, indices = index.search(query_embeddings, k)
    return distances, indices

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

    # Create a Faiss index
    embedding_dim = embeddings.shape[1]
    index = create_faiss_index(embedding_dim)

    # Add embeddings to the Faiss index
    add_embeddings_to_index(index, embeddings)

    # Save the index to a file
    faiss.write_index(index, "embeddings.index")
    print("Faiss index saved to embeddings.index")

    # Example query
    query_texts = ["Electric vehicles and renewable energy."]
    query_embeddings = generate_embeddings(model, query_texts)

    # Search for similar embeddings
    distances, indices = search_similar_embeddings(index, query_embeddings)
    print("Top similar embeddings indices:", indices)
    print("Top similar embeddings distances:", distances)
