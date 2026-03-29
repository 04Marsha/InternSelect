# InternSelect

### AI-Powered Internship Shortlisting Predictor

> **Where skills matter more than scores**

---

## 🔗 Live Demo

👉 https://internselect.onrender.com

---

## ⚠️ Note on Initial Load Time

> Due to deployment on the **free tier of Render**, the application may take **30–60 seconds to load on the first request**.

* The server automatically goes into a **sleep state** after inactivity
* The first request “wakes up” the server, causing a slight delay
* Subsequent requests are **fast and responsive**

👉 This is a limitation of the hosting plan, not the application itself.


---

## 📌 Overview

**InternSelect** is a full-stack, end-to-end Machine Learning web application that predicts whether a student is likely to be shortlisted for an internship.

Unlike traditional systems that overemphasize CGPA, InternSelect evaluates a candidate holistically using academic performance, technical skills, and practical experience.

---

## 🎯 Problem Statement

Internship shortlisting is often perceived as being heavily dependent on CGPA. However, real-world hiring considers multiple factors:

* 💻 Problem-solving ability (DSA)
* 📂 Project experience
* 🧠 Technical breadth
* 🏆 Hackathon participation
* 🎓 Academic performance

### 👉 Objective

Build a system that predicts internship shortlisting using multi-dimensional candidate evaluation.

---

## 🧠 Key Features

* 🔮 ML-based shortlisting prediction
* 💡 Actionable recommendations for improvement
* 🧠 Explainable AI (SHAP-based insights)
* 📊 Interactive feature impact visualization (Plotly)
* ⚡ Real-time prediction via web interface
* 🌐 Fully deployed cloud application

---

## 📊 Dataset

Since real hiring datasets are not publicly available, a synthetic dataset was generated to simulate realistic scenarios.

### 🔹 Features

| Feature                 | Description                     |
| ----------------------- | ------------------------------- |
| `cgpa`                  | Academic score (5.5 – 9.5)      |
| `num_projects`          | Number of completed projects    |
| `dsa_level`             | Problem-solving level (0–3)     |
| `tech_stack_count`      | Number of technologies known    |
| `hackathon`             | Participation (0 / 1)           |
| `internship_experience` | Prior internship (0 / 1)        |
| `github_activity`       | GitHub activity level           |
| `deployed_projects`     | Live project deployment (0 / 1) |
| `project_complexity`    | Project sophistication (1–3)    |
| `shortlisted`           | Target variable                 |

---

## 🔍 Exploratory Data Analysis

EDA was performed to:

* Understand feature distributions
* Analyze class imbalance
* Identify correlations
* Detect overlapping decision boundaries

### 🔑 Insights

* CGPA alone is not sufficient
* DSA + projects significantly impact selection
* Real-world ambiguity improves model robustness

---

## 🤖 Model Development

### Models Trained

| Model               | Description                     |
| ------------------- | ------------------------------- |
| Decision Tree       | Baseline (overfitting observed) |
| Tuned Decision Tree | Reduced variance                |
| Random Forest       | Final selected model            |

---

### 📈 Performance

| Model               | Train Accuracy | Test Accuracy |
| ------------------- | -------------- | ------------- |
| Decision Tree       | 1.00           | 0.70          |
| Tuned Decision Tree | 0.94           | 0.75          |
| Random Forest       | **0.97**       | **0.82**      |

👉 **Final Model: Random Forest**
✔ Best generalization
✔ Stable predictions
✔ Handles feature interactions well

---

## 🧠 Explainable AI (SHAP)

InternSelect integrates **SHAP (SHapley Additive exPlanations)** to provide:

* 📊 Feature impact visualization
* 📈 Positive vs negative contribution
* 🧠 Personalized reasoning

### Example Output

* “Internship experience increased your chances by 18% ⬆️”
* “Low CGPA decreased your chances by 12% ⬇️”

👉 Makes predictions **transparent and interpretable**

---

## 🌐 Web Application

### 🖥️ Frontend

* HTML + CSS (custom design)
* Clean and responsive UI
* Real-time feedback

### ⚙️ Backend

* Flask framework
* Model inference using `joblib`
* Session-based state handling
* POST → Redirect → GET pattern

---

## 🔄 User Flow

1. User enters profile details
2. Model predicts outcome
3. Displays:

   * 🎯 Prediction result
   * 💡 Recommendations
   * 🧠 AI explanations
   * 📊 SHAP graph

---

## 🔐 Security & Best Practices

* Environment variables for secrets
* .gitignore for sensitive files
* Clean project structure
* No hardcoded credentials

---

## 🚀 Deployment

* Platform: **Render (Free Tier)**
* Hosted as a live web app
* Accessible globally

---

## 🛠️ Tech Stack

* **Language:** Python
* **ML:** Scikit-learn
* **Data:** Pandas, NumPy
* **Explainability:** SHAP
* **Visualization:** Plotly
* **Backend:** Flask
* **Frontend:** HTML, CSS
* **Deployment:** Render
* **Version Control:** Git & GitHub

---

## 📌 Project Highlights

✔ End-to-end ML pipeline
✔ Realistic synthetic dataset
✔ Explainable AI integration
✔ Interactive visualizations
✔ Production-ready deployment

---

## 👨‍💻 Author

**Marsha Sharma**

---

