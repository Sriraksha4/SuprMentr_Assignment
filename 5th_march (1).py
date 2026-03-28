import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Age": [19, 21, 23, 31, 45, 52, 23, 40, 60, 48],
    "Annual Income": [15, 16, 17, 18, 60, 62, 64, 65, 70, 68],
    "Spending Score": [39, 40, 42, 43, 80, 82, 85, 88, 90, 87]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Apply KMeans
X = df[["Annual Income", "Spending Score"]]
kmeans = KMeans(n_clusters=2, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)

# Display centroids
print("\nCentroids:")
print(kmeans.cluster_centers_)

# Plot clusters
plt.scatter(df["Annual Income"], df["Spending Score"], c=df["Cluster"])

# Plot centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Mall Customer Segmentation")
plt.show()