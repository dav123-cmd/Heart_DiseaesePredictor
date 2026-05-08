
from django.db import models

class HeartData(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField(choices=[(1, "Male"), (0, "Female")])
    cp = models.IntegerField(choices=[
        (0, "Typical Angina"),
        (1, "Atypical Angina"),
        (2, "Non-anginal Pain"),
        (3, "Asymptomatic"),
    ])
    trestbps = models.IntegerField()  # Resting blood pressure
    chol = models.IntegerField()      # Cholesterol
    fbs = models.IntegerField(choices=[(1, "True"), (0, "False")])  # Fasting blood sugar
    restecg = models.IntegerField(choices=[
        (0, "Normal"),
        (1, "ST-T Abnormality"),
        (2, "Left Ventricular Hypertrophy"),
    ])
    thalach = models.IntegerField()   # Max heart rate
    exang = models.IntegerField(choices=[(1, "Yes"), (0, "No")])  # Exercise induced angina
    oldpeak = models.FloatField()     # ST depression
    slope = models.IntegerField(choices=[
        (0, "Upsloping"),
        (1, "Flat"),
        (2, "Downsloping"),
    ])
    ca = models.IntegerField()        # Number of major vessels (0–3)
    thal = models.IntegerField(choices=[
        (1, "Normal"),
        (2, "Fixed Defect"),
        (3, "Reversible Defect"),
    ])

    # Optional: prediction result field
    prediction = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"HeartData (Age: {self.age}, Sex: {self.sex})"
