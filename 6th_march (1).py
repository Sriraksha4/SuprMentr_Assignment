import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Create dataset
data = {
    "income": [25000, 40000, 50000, 60000, 70000, 80000, 30000, 45000],
    "credit_score": [600, 650, 700, 750, 800, 720, 680, 710],
    "loan_amount": [10000, 15000, 20000, 25000, 30000, 22000, 12000, 18000],
    "employment_years": [1, 2, 3, 5, 7, 4, 2, 3],
    "loan_approved": [0, 0, 1, 1, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

# Features and Target
X = df[["income", "credit_score", "loan_amount", "employment_years"]]
y = df["loan_approved"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate accuracy
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Predict new customer
new_customer = [[55000, 720, 20000, 4]]
prediction = model.predict(new_customer)

print("Loan Approved (1=Yes, 0=No):", prediction[0])