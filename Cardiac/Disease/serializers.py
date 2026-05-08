from rest_framework import serializers
from .models import HeartData

class HeartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartData
        fields = [
            "id", "age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak", "slope",
            "ca", "thal", "prediction"
        ]
