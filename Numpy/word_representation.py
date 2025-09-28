import numpy as np

sentences = ["i love ai", "ai loves me"]

tokens = [s.split() for s in sentences]
print("Tokens:", tokens)

vocab = list(set([word for sent in tokens for word in sent]))
print("Vocabulary:", vocab)

word_to_idx = {word: i for i, word in enumerate(vocab)}
print("Word to Index:", word_to_idx)

vocab_size = len(vocab)
word = "ai"
one_hot = np.zeros(vocab_size)
one_hot[word_to_idx[word]] = 1
print("\nOne-hot for 'ai':", one_hot)

embedding_dim = 5
embedding_matrix = np.random.randn(vocab_size, embedding_dim)

print("\nEmbedding matrix:\n", embedding_matrix)

word_vec = embedding_matrix[word_to_idx["love"]]
print("\nVector for 'love':", word_vec)

