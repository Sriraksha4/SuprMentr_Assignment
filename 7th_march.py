from sklearn.neighbors import NearestNeighbors
import numpy as np

# 1. Take User Input for Dataset Size
rows = int(input("Enter number of users: "))
cols = int(input("Enter number of genres (e.g., Action, Comedy, Thriller): "))

user_data = []

# 2. Collect Data for each User
for i in range(rows):
    print(f"\nEnter preferences for User {i} (1 for Like, 0 for Dislike):")
    prefs = []
    for j in range(cols):
        val = int(input(f"  Genre {j+1}: "))
        prefs.append(val)
    user_data.append(prefs)

data = np.array(user_data)

# 3. Initialize and Train KNN
# Find the 2 nearest neighbors (including the user themselves)
model = NearestNeighbors(n_neighbors=2)
model.fit(data)

# 4. Find matches for a specific user
target_user = int(input(f"\nEnter the User index to find neighbors for (0 to {rows-1}): "))
distances, indices = model.kneighbors([data[target_user]])

print("\n--- Results ---")
print(f"Nearest Neighbors for User {target_user} (indices):", indices[0])
print("Similarity Distances:", distances[0])