import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import joblib

# Load preprocessed data
df = pd.read_csv('preprocessed_data.csv')

# Encode categorical variables
le = LabelEncoder()
for column in ['preferredLabel_en', 'preferredLabel_de']:
    df[column] = le.fit_transform(df[column])

# Split the dataset
X = df[['experience_order', 'preferredLabel_en']]
y = df['preferredLabel_skills']

# Initialize and train the Random Forest model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# Make predictions
y_pred = rf_model.predict(X)

# Print model performance
print("Accuracy:", accuracy_score(y, y_pred))
print("\nClassification Report:")
print(classification_report(y, y_pred))

# After training your model
rf_model.fit(X, y)

# Save the trained model
joblib.dump(rf_model, 'trained_model.joblib')
