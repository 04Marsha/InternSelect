import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, flash
import joblib
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "secret_key")
SHORTLIST_THRESHOLD = 0.45

model = joblib.load("model/model.pkl")

def generate_recommendations(model, base_input, base_confidence):
    recommendations = []

    test_changes = {
        "dsa_level": min(base_input["dsa_level"] + 1, 3),
        "num_projects": base_input["num_projects"] + 1,
        "tech_stack_count": base_input["tech_stack_count"] + 1,
        "hackathon": 1
    }

    human_readable = {
        "dsa_level": "DSA level",
        "num_projects": "number of projects",
        "tech_stack_count": "tech stack breadth",
        "hackathon": "hackathon participation"
    }

    for feature, new_value in test_changes.items():
        modified_input = base_input.copy()
        modified_input[feature] = new_value

        df = pd.DataFrame([modified_input])
        new_confidence = model.predict_proba(df)[0][1]

        gain = (new_confidence - base_confidence) * 100

    
        if gain > 5:
            label = human_readable.get(feature, feature.replace("_", " "))
            recommendations.append(f"Improving your {label} could increase your shortlisting chances by ~{gain:.1f}%")
            
    return recommendations


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    cgpa = float(request.form['cgpa'])
    num_projects = int(request.form['num_projects'])
    dsa_level = int(request.form['dsa_level'])
    tech_stack_count = int(request.form['tech_stack_count'])
    hackathon = int(request.form['hackathon'])

    features = pd.DataFrame([{
        "cgpa": cgpa,
        "num_projects": num_projects,
        "dsa_level": dsa_level,
        "tech_stack_count": tech_stack_count,
        "hackathon": hackathon
}])

    proba = model.predict_proba(features)[0]
    confidence = proba[1]
    prediction = int(confidence >= SHORTLIST_THRESHOLD)
    base_input = {
        "cgpa": cgpa,
        "num_projects": num_projects,
        "dsa_level": dsa_level,
        "tech_stack_count": tech_stack_count,
        "hackathon": hackathon
    }
    recommendations = []

    if prediction == 0 or confidence < 0.6:
        recommendations = generate_recommendations(model, base_input, confidence)

    result = (
        f"Shortlisted 🎉 (Confidence: {confidence*100:.1f}%)"
        if prediction == 1
        else f"Not Shortlisted ❌ (Confidence: {(1-confidence)*100:.1f}%)"
    )
    if prediction == 1:
        flash(result, "success")
    else:
        flash(result, "failure")
        for rec in recommendations:
            flash("💡 " + rec, "failure")

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
