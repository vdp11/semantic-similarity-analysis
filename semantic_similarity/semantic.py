import spacy

# Load the language model
nlp = spacy.load("en_core_web_md")

# Define words or phrases to compare
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Calculate similarities
similarity_cat_monkey = word1.similarity(word2)
similarity_cat_banana = word1.similarity(word3)

# Print the results
print("Similarity between 'cat' and 'monkey':", similarity_cat_monkey)
print("Similarity between 'cat' and 'banana':", similarity_cat_banana)
