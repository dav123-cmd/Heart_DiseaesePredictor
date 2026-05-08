
from django.shortcuts import render
from .models import HeartData
from .serializers import HeartDataSerializer
import joblib
import numpy as np

# Load scaler and model once
scaler = joblib.load("scaler.pkl")
model = joblib.load("random_forest_heart.pkl")
def home (request):
    return render(request,'home.html')

def result(request):
    return render(request,'result.html')


def submit_heart_data(request):
    if request.method == "POST":
        serializer = HeartDataSerializer(data=request.POST)
        if serializer.is_valid():
            heart_data = serializer.save()

            # Prepare features
            features = np.array([[
                heart_data.age,
                heart_data.sex,
                heart_data.cp,
                heart_data.trestbps,
                heart_data.chol,
                heart_data.fbs,
                heart_data.restecg,
                heart_data.thalach,
                heart_data.exang,
                heart_data.oldpeak,
                heart_data.slope,
                heart_data.ca,
                heart_data.thal,
            ]])

            # Scale and predict
            features_scaled = scaler.transform(features)
            prediction = model.predict(features_scaled)[0]

            # Get both probabilities
            if hasattr(model, "predict_proba"):
                proba = model.predict_proba(features_scaled)[0]
                no_disease_prob = proba[0] * 100
                disease_prob = proba[1] * 100
            else:
                no_disease_prob = None
                disease_prob = None

            heart_data.prediction = int(prediction)
            heart_data.save()

            # Render result page with both probabilities
            return render(request, "result.html", {
                "prediction": heart_data.prediction,
                "no_disease_prob": no_disease_prob,
                "disease_prob": disease_prob,
                "patient": heart_data
            })

    return render(request, "form.html", {"error": "Invalid submission"})
