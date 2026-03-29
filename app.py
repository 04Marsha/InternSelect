import pandas as pd
import numpy as np
import matplotlib

from shap_explanation import shap_explanation
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
import joblib
import shap
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "secret_key")
SHORTLIST_THRESHOLD = 0.45

model = joblib.load("model/model.pkl")
explainer = shap.TreeExplainer(model)

def generate_recommendations(model, base_input, base_confidence):
    recommendations = []

    test_changes = {
        "dsa_level": min(base_input["dsa_level"] + 1, 3),
        "num_projects": base_input["num_projects"] + 1,
        "tech_stack_count": base_input["tech_stack_count"] + 1,
        "hackathon": 1,
        "internship_experience": 1,
        "github_activity": base_input["github_activity"] + 5,
        "deployed_projects": 1,
        "project_complexity": min(base_input["project_complexity"] + 1, 3)
    }

    human_readable = {
        "internship_experience": "getting an internship",
        "github_activity": "increasing your GitHub activity",
        "deployed_projects": "deploying your projects",
        "project_complexity": "building more advanced projects",
        "dsa_level": "improving your DSA skills",
        "num_projects": "adding more projects",
        "tech_stack_count": "learning more technologies",
        "hackathon": "participating in hackathons"
    }

    improvements = []

    for feature, new_value in test_changes.items():
        modified_input = base_input.copy()
        modified_input[feature] = new_value

        df = pd.DataFrame([modified_input])
        new_confidence = model.predict_proba(df)[0][1]

        gain = round((new_confidence - base_confidence) * 100, 1)
    
        if gain > 0:
            label = human_readable.get(feature, feature.replace("_", " "))
            improvements.append((gain, label))

    improvements.sort(reverse=True)

    recommendations = [f"{label.capitalize()} could increase your shortlisting chances by {gain:.1f}%" for gain, label in improvements[:3]]        
    return recommendations


def get_feature_importance(model, input_df):
    importances = model.feature_importances_
    feature_names = input_df.columns

    feature_impact = list(zip(feature_names, importances))

    feature_impact.sort(key=lambda x: x[1], reverse=True)

    explanations = []

    for feature, importance in feature_impact[:3]:
        explanations.append(f"{feature.replace('_',' ').title()} had a strong impact")

    return explanations

def explain_prediction(input_data):
    explanations = []

    if input_data["internship_experience"] == 1:
        explanations.append("Your internship experience boosted your profile")
    else:
        explanations.append("Lack of internship experience hurt your chances")

    if input_data["github_activity"] > 20:
        explanations.append("Strong GitHub activity improved your chances")
    elif input_data["github_activity"] < 5:
        explanations.append("Low GitHub activity weakened your profile")

    if input_data["cgpa"] > 8:
        explanations.append("High CGPA strengthened your profile 🎓")
    elif input_data["cgpa"] >= 6.5:
        explanations.append("Decent CGPA had a moderate impact")
    else:
        explanations.append("Low CGPA significantly hurt your chances")

    if input_data["num_projects"] >= 3:
        explanations.append("Good number of projects improved your profile")
    elif input_data["num_projects"] == 0:
        explanations.append("No projects weakened your profile")

    if input_data["deployed_projects"] == 1:
        explanations.append("Deployed projects boosted your chances")
    else:
        explanations.append("Lack of deployed projects reduced your impact")

    if input_data["project_complexity"] == 3:
        explanations.append("Advanced projects gave you an edge")
    elif input_data["project_complexity"] == 1:
        explanations.append("Basic projects limited your profile strength")

    return explanations

@app.route("/")
def home():
    return render_template("index.html", currentYear=datetime.now().year)

@app.route("/predict")
def form():
    return render_template("form.html", currentYear=datetime.now().year)

@app.route("/result")
def analysis():
    plot_html = session.get("plot_html", None)
    return render_template(
        "analysis.html",
        currentYear=datetime.now().year,
        plot_html=plot_html
    )

@app.route("/predict", methods=["POST"])
def predict():
    cgpa = float(request.form['cgpa'])
    num_projects = int(request.form['num_projects'])
    dsa_level = int(request.form['dsa_level'])
    tech_stack_count = int(request.form['tech_stack_count'])
    hackathon = int(request.form['hackathon'])
    internship_experience = int(request.form['internship_experience'])
    github_activity = int(request.form['github_activity'])
    deployed_projects = int(request.form['deployed_projects'])
    project_complexity = int(request.form['project_complexity'])

    features = pd.DataFrame([{
        "cgpa": cgpa,
        "num_projects": num_projects,
        "dsa_level": dsa_level,
        "tech_stack_count": tech_stack_count,
        "hackathon": hackathon,
        "internship_experience": internship_experience,
        "github_activity": github_activity,
        "deployed_projects": deployed_projects,
        "project_complexity": project_complexity
}])

    proba = model.predict_proba(features)[0]
    confidence = proba[1]
    prediction = int(confidence >= SHORTLIST_THRESHOLD)
    base_input = {
        "cgpa": cgpa,
        "num_projects": num_projects,
        "dsa_level": dsa_level,
        "tech_stack_count": tech_stack_count,
        "hackathon": hackathon,
        "internship_experience": internship_experience,
        "github_activity": github_activity,
        "deployed_projects": deployed_projects,
        "project_complexity": project_complexity
    }
    recommendations = []

    if prediction == 0 or confidence < 0.6:
        recommendations = generate_recommendations(model, base_input, confidence)

    explanations, plot_html = shap_explanation(model, explainer, features)

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

    for exp in explanations:
        flash("🧠 " + exp, "success")

    session["plot_html"] = plot_html

    return redirect(url_for("analysis"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
