import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, f1_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# ================================
# Load Dataset
# ================================
df = pd.read_csv("Employee-Attrition.csv")

# Target column
y = df["Attrition"].map({"Yes": 1, "No": 0})  # Convert to 0/1
X = df.drop(columns=["Attrition", "EmployeeNumber"])  # drop ID, target

# ================================
# Identify categorical & numeric
# ================================
categorical = X.select_dtypes(include=["object"]).columns.tolist()
numeric = X.select_dtypes(exclude=["object"]).columns.tolist()

# ================================
# Preprocessing
# ================================
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
])

# ================================
# Candidate Models
# ================================
models = {
    "RandomForest": RandomForestClassifier(),
    "GradientBoost": GradientBoostingClassifier(),
    "DecisionTree": DecisionTreeClassifier(),
    "LogisticRegression": LogisticRegression(max_iter=500)
}

best_model = None
best_score = -1
results = {}

for name, model in models.items():
    pipeline = Pipeline([
        ("preprocess", preprocessor),
        ("clf", model)
    ])
    
    scores = cross_val_score(pipeline, X, y, cv=5, scoring="f1")
    avg_score = scores.mean()
    results[name] = avg_score
    
    print(f"{name}: F1 = {avg_score:.4f}")
    
    if avg_score > best_score:
        best_score = avg_score
        best_model = pipeline

# ================================
# Final Train + Save Best Model
# ================================
best_model.fit(X, y)
with open("best_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

print("\n✅ Training complete. Best model saved as best_model.pkl")
print("Model Scores:", results)
