from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Dataset (20+ sentences)
reviews = [
    "This movie is amazing",
    "I loved the film",
    "Great acting and story",
    "Fantastic experience",
    "Very enjoyable movie",

    "The movie was boring",
    "I hated the film",
    "Worst movie ever",
    "Not interesting at all",
    "Terrible acting",

    "The movie was okay",
    "It was average",
    "Nothing special",
    "Just fine",
    "It was normal",

    "Excellent direction",
    "Loved the music",
    "Bad screenplay",
    "Mediocre performance",
    "Superb visuals"
]

# Labels
labels = [
    "Positive", "Positive", "Positive", "Positive", "Positive",
    "Negative", "Negative", "Negative", "Negative", "Negative",
    "Neutral", "Neutral", "Neutral", "Neutral", "Neutral",
    "Positive", "Positive", "Negative", "Neutral", "Positive"
]

# Convert text to numbers using TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(reviews)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Test model
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Try new input
new_review = ["The movie was fantastic and enjoyable"]
new_vec = vectorizer.transform(new_review)
prediction = model.predict(new_vec)

print("Prediction:", prediction[0])