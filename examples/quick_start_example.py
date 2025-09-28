#!/usr/bin/env python3
"""
Quick Start Example: ML Pipeline in 50 Lines
============================================

This script demonstrates a complete ML pipeline using the techniques
from the training notebook in a condensed, production-ready format.

Usage:
    python examples/quick_start_example.py
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib

def main():
    """Demonstrate complete ML pipeline"""

    print("🚀 Quick Start ML Pipeline Example")
    print("=" * 40)

    # 1. Create synthetic dataset (replace with your data)
    print("📊 Creating dataset...")
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=10,
        n_redundant=10,
        random_state=42
    )

    # Convert to DataFrame for realistic workflow
    feature_names = [f'feature_{i:02d}' for i in range(X.shape[1])]
    X_df = pd.DataFrame(X, columns=feature_names)

    print(f"Dataset shape: {X_df.shape}")
    print(f"Target distribution: {np.bincount(y)}")

    # 2. Split data
    print("\n🔀 Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X_df, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3. Create ML pipeline
    print("\n🏗️ Building ML pipeline...")
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    # 4. Train with cross-validation
    print("\n🎯 Training model...")
    cv_scores = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='accuracy')
    print(f"Cross-validation accuracy: {cv_scores.mean():.3f} (+/- {cv_scores.std() * 2:.3f})")

    # 5. Final training and evaluation
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    test_accuracy = accuracy_score(y_test, y_pred)
    print(f"\n📊 Test Results:")
    print(f"Test accuracy: {test_accuracy:.3f}")

    # 6. Feature importance
    feature_importance = pipeline.named_steps['classifier'].feature_importances_
    top_features = sorted(zip(feature_names, feature_importance),
                         key=lambda x: x[1], reverse=True)[:5]

    print(f"\n🔍 Top 5 Important Features:")
    for feature, importance in top_features:
        print(f"  {feature}: {importance:.3f}")

    # 7. Save model
    model_path = 'models/quick_start_model.pkl'
    joblib.dump(pipeline, model_path)
    print(f"\n💾 Model saved to: {model_path}")

    # 8. Demonstrate prediction
    print(f"\n🔮 Making predictions...")
    sample_predictions = pipeline.predict(X_test[:5])
    sample_probabilities = pipeline.predict_proba(X_test[:5])

    print("Sample predictions:")
    for i, (pred, prob) in enumerate(zip(sample_predictions, sample_probabilities)):
        confidence = prob.max()
        print(f"  Sample {i+1}: Class {pred} (confidence: {confidence:.3f})")

    print(f"\n✅ Pipeline complete! Ready for production deployment.")

    return pipeline, test_accuracy

if __name__ == "__main__":
    # Create models directory if it doesn't exist
    import os
    os.makedirs('models', exist_ok=True)

    # Run the pipeline
    model, accuracy = main()

    print(f"\n🎉 Success! Final model accuracy: {accuracy:.3f}")