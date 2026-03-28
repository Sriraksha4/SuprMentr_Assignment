import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Create dataset (with missing values & duplicates)
data = {
    "Age": [25, 30, None, 35, 30, 40],
    "Salary": [50000, 60000, 55000, None, 60000, 70000],
    "City": ["Hyderabad", "hyderabad", None, "HYDERABAD", "Hyderabad", "Delhi"],
    "Experience": [2, 5, 3, 7, 5, 10]   # duplicate: (30,60000,...,5)
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Handle missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].mean(), inplace=True)
df["City"].fillna("Unknown", inplace=True)

# 3. Standardize city names (lowercase)
df["City"] = df["City"].str.lower()

# 4. Apply Min-Max Scaling
scaler = MinMaxScaler()
df[["Age", "Salary"]] = scaler.fit_transform(df[["Age", "Salary"]])
print("\nCleaned Data:")
print(df)