from textblob import TextBlob

# 5 movie reviews
reviews = [
    "The movie was fantastic and full of excitement.",
    "I really loved the acting and story.",
    "The film was average, nothing special.",
    "It was boring and too long.",
    "The movie was terrible and disappointing."
]

print("Movie Review Sentiment Analyzer\n")

for i, review in enumerate(reviews):
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Review {i+1}: {review}")
    print(f"Sentiment: {sentiment}")
    print(f"Polarity Score: {polarity:.2f}")
    print("-" * 50)