import numpy as np


def create_embedding(word, dimension=50):
    seed = abs(hash(word)) % (2**32)

    rng = np.random.default_rng(seed)

    vector = rng.normal(0, 1, dimension)

    norm = np.linalg.norm(vector)

    if norm != 0:
        vector = vector / norm

    return vector


def create_embeddings(words):
    embeddings = []

    for word in words:
        embeddings.append(create_embedding(word))

    if len(embeddings) == 0:
        return np.array([])

    return np.array(embeddings)