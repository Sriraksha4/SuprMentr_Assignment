from sklearn.feature_extraction.text import TfidfVectorizer

# 5 sample documents
documents = [
    "Machine learning helps computers learn from data.",
    "Natural language processing helps computers understand text.",
    "Deep learning is a part of machine learning.",
    "Text mining and NLP are useful for document analysis.",
    "Artificial intelligence includes machine learning and NLP."
]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

# Get feature names
feature_names = vectorizer.get_feature_names_out()

# Print TF-IDF top words for each document
for i, doc in enumerate(documents):
    print(f"\nDocument {i+1}: {doc}")
    tfidf_scores = tfidf_matrix[i].toarray()[0]
    
    # Get top 5 keywords
    top_indices = tfidf_scores.argsort()[-5:][::-1]
    
    print("Top Keywords:")
    for idx in top_indices:
        if tfidf_scores[idx] > 0:
            print(f"{feature_names[idx]} : {tfidf_scores[idx]:.3f}")

print("\nExplanation:")
print("TF-IDF stands for Term Frequency-Inverse Document Frequency.")
print("It helps identify important words in a document by reducing common words and highlighting unique words.")