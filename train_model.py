# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv('dataset/Training.csv')

# Separate features and target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Encode the target column (diseases)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model & label encoder
joblib.dump(model, 'model/rf_model.joblib')
joblib.dump(le, 'model/label_encoder.joblib')