import sqlite3
import numpy as np

def save_embeddings_to_database(embeddings, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create a table to store embeddings
    cursor.execute('''CREATE TABLE IF NOT EXISTS embeddings
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       embedding BLOB)''')

    # Insert embeddings into the table
    for embedding in embeddings:
        cursor.execute('''INSERT INTO embeddings (embedding) VALUES (?)''', (sqlite3.Binary(embedding.tobytes()),))

    conn.commit()
    conn.close()

def load_embeddings_from_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Retrieve embeddings from the database
    cursor.execute('''SELECT embedding FROM embeddings''')
    rows = cursor.fetchall()

    embeddings = []
    for row in rows:
        embedding = np.frombuffer(row[0], dtype=np.float32)
        embeddings.append(embedding)

    conn.close()
    return embeddings

# Example usage:
embeddings = np.array([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])  # Example embeddings array
save_embeddings_to_database(embeddings, "embeddings.db")

loaded_embeddings = load_embeddings_from_database("embeddings.db")
