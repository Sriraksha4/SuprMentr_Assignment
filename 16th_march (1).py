from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

# Dataset
sentences = [
    "I love this movie",
    "This movie is terrible",
    "Amazing acting",
    "Worst film ever"
]

# 🔹 1. Bag of Words
bow = CountVectorizer()
bow_matrix = bow.fit_transform(sentences)

print("=== Bag of Words Matrix ===")
print(bow_matrix.toarray())
print("Features:", bow.get_feature_names_out())

# 🔹 2. TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(sentences)

print("\n=== TF-IDF Matrix ===")
print(tfidf_matrix.toarray())
print("Features:", tfidf.get_feature_names_out())

# 🔹 3. Convert to DataFrame (Extra visualization)
bow_df = pd.DataFrame(bow_matrix.toarray(), columns=bow.get_feature_names_out())
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out())

print("\n=== Bag of Words DataFrame ===")
print(bow_df)

print("\n=== TF-IDF DataFrame ===")
print(tfidf_df)

# 🔹 4. Comparison
print("\n=== Comparison ===")
print("Bag of Words shows frequency of words.")
print("TF-IDF shows importance of words (less common words get higher value).")