# Libraries
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib

# ML algorithms
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA

# Store models in dictionary
models = {
    "Random Forest": RandomForestClassifier(n_estimators=100),
    "Naive Bayes": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(max_depth=5),
    "Neural Network (MLP)": MLPClassifier(hidden_layer_sizes=(20,20), max_iter=1000),
    "PCA + Logistic Regression": LogisticRegression(max_iter=1000),
}
results = {}

# Load dataset
df = pd.read_csv('heart.csv')
df = df.dropna(subset=['target'])  # clean data

X = df.drop('target', axis=1)
y = df['target']

# Train/test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardization
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# PCA for dimensionality reduction
pca = PCA(n_components=5)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# Train and evaluate models
for name, model in models.items():
    if name == "PCA + Logistic Regression":
        model.fit(X_train_pca, y_train)
        y_pred = model.predict(X_test_pca)
        y_proba = model.predict_proba(X_test_pca)[:,1]
    else:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        if hasattr(model, "predict_proba"):
            y_proba = model.predict_proba(X_test_scaled)[:,1]
        else:
            y_proba = model.decision_function(X_test_scaled)

    acc = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)
    results[name] = (acc, auc)

    # Save each model
    joblib.dump(model, f"{name.replace(' ', '_').lower()}_heart.pkl")

# Save scaler
joblib.dump(scaler, "scaler.pkl")

# Print results
for name, (acc, auc) in results.items():
    print(f"{name}: Accuracy={acc:.2f}, AUC-ROC={auc:.2f}")

print("All models and scaler saved successfully")
