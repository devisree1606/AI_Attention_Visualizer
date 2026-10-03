import numpy as np


def calculate_attention(embeddings):
    if embeddings is None or len(embeddings) == 0:
        return np.array([])

    query = np.mean(embeddings, axis=0)

    scores = np.dot(embeddings, query)

    scores = scores - np.max(scores)

    exp_scores = np.exp(scores)

    attention = exp_scores / np.sum(exp_scores)

    return attention