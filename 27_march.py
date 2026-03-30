# 5 word pairs with semantic meaning explanation

word_pairs = [
    ("car", "automobile", "These words are highly similar because both refer to the same type of vehicle."),
    ("king", "queen", "These words are semantically related because both represent royal titles."),
    ("dog", "puppy", "These words are related because a puppy is a young dog."),
    ("book", "novel", "These words are similar because a novel is a type of book."),
    ("teacher", "student", "These words are related because they are connected in an educational context.")
]

print("Semantic Meaning Analysis\n")

for i, (word1, word2, explanation) in enumerate(word_pairs, start=1):
    print(f"Pair {i}: {word1} - {word2}")
    print(f"Explanation: {explanation}")
    print("-" * 60)