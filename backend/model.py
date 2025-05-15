# backend/model.py

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv('backend/loan_dataset.csv')

# Encode categorical columns
le = LabelEncoder()
for col in ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status']:
    df[col] = le.fit_transform(df[col])

# Features and target
X = df.drop(['Loan_Status'], axis=1)
y = df['Loan_Status']

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and label encoder
with open('backend/loan_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('backend/label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

print("✅ Model trained and saved.")
