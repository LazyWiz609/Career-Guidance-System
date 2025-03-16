import pandas as pd
from datasets import load_dataset
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# Load the dataset
dataset = load_dataset("ElenaSenger/Karrierewege")

# Convert to pandas DataFrame and take a smaller subset
df = dataset['train'].to_pandas().head(1000)  # Process only the first 1000 rows

# Handle missing values
df = df.dropna(subset=['preferredLabel_en'])

# Normalize text
df['preferredLabel_en'] = df['preferredLabel_en'].str.lower().str.strip()
df['preferredLabel_de'] = df['preferredLabel_de'].str.lower().str.strip()

# Encode categorical variables
le = LabelEncoder()
df['encoded_experience'] = le.fit_transform(df['experience_order'])

# Scale numerical features
scaler = StandardScaler()
df['scaled_id'] = scaler.fit_transform(df[['_id']])

# Split the dataset
X = df[['_id', 'experience_order', 'preferredLabel_en', 'preferredLabel_de']]
y = df['preferredLabel_skills']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(df.head())
print(df.columns)
print(X_train.shape, X_test.shape)
df.to_csv('preprocessed_data.csv', index=False)

