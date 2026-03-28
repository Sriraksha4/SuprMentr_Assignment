import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle

# Create dataset
data = {
    "Income": [25000, 40000, 50000, 60000, 70000, 80000, 30000, 45000],
    "Credit Score": [600, 650, 700, 750, 800, 720, 680, 710],
    "Age": [22, 25, 30, 35, 40, 45, 28, 32],
    "Loan Amount": [10000, 15000, 20000, 25000, 30000, 22000, 12000, 18000],
    "Employment Years": [1, 2, 3, 5, 7, 4, 2, 3],
    "Approved": [0, 0, 1, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

# Features and Target
X = df[["Income", "Credit Score", "Age", "Loan Amount", "Employment Years"]]
y = df["Approved"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

# Train Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Compare accuracy
dt_acc = dt.score(X_test, y_test)
rf_acc = rf.score(X_test, y_test)

print("Decision Tree Accuracy:", dt_acc)
print("Random Forest Accuracy:", rf_acc)

# Feature importance (Random Forest)
importance = rf.feature_importances_
print("\nFeature Importance:")
for col, val in zip(X.columns, importance):
    print(col, ":", val)

# Save model using pickle
with open("loan_model.pkl", "wb") as f:
    pickle.dump(rf, f)
print("\nModel saved as loan_model.pkl")