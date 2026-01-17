from flask import Flask, render_template, request, redirect, url_for, flash
import joblib
import numpy as np
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "secret_key")

model = joblib.load("model/model.pkl")

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

    features = np.array([[cgpa, num_projects, dsa_level, tech_stack_count, hackathon]])
    prediction = model.predict(features)[0]

    result = "Shortlisted 🎉" if prediction == 1 else "Not Shortlisted ❌"

    flash(result)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
