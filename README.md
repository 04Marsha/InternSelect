# InternSelect

**Where skills matter more than scores**

InternSelect is an end-to-end machine learning web application that predicts whether a student is likely to be shortlisted for an internship, based on multiple academic and skill-based factors rather than CGPA alone.

The project demonstrates the complete ML lifecycle - from data generation and exploratory data analysis to model training, evaluation, web integration, and secure cloud deployment.

🔗 **Live Demo:** [https://internselect.onrender.com](https://internselect.onrender.com)

---

## Problem Statement

Internship shortlisting is often perceived as being heavily dependent on CGPA. However, in real-world hiring, recruiters evaluate candidates using a combination of factors such as:

* Problem-solving ability (DSA)
* Practical exposure through projects
* Breadth of technical skills
* Participation in hackathons
* Academic consistency

**Objective:**
Build a machine learning system that evaluates a student profile holistically and predicts whether the student is likely to be shortlisted for an internship.

---

## Dataset Description

Since real hiring datasets are rarely public, a synthetic dataset was generated to closely simulate realistic internship shortlisting scenarios.

### Features

| Feature            | Description                                            |
| ------------------ | ------------------------------------------------------ |
| cgpa               | Student CGPA (5.5 – 9.5)                               |
| num_projects       | Number of completed projects                           |
| dsa_level          | DSA proficiency level (0–3)                            |
| tech_stack_count   | Number of technologies known                           |
| hackathon          | Hackathon participation (0 = No, 1 = Yes)              |
| shortlisted        | Target variable (0 = Not Shortlisted, 1 = Shortlisted) |

The dataset intentionally includes noise and overlapping classes to reflect real-world ambiguity and avoid unrealistically perfect models.

---

## Exploratory Data Analysis (EDA)

EDA was performed to:

* Understand feature distributions
* Examine class balance
* Analyze overlap between shortlisted and non-shortlisted candidates
* Identify important predictive features

### Key Observations

* CGPA alone is not sufficient for prediction
* DSA proficiency and project experience play a major role
* Feature overlap is expected and helps improve generalization

---

## Model Development

### Models Trained

1. Decision Tree Classifier

   * Baseline model
   * High training accuracy
   * Overfitting observed

2. Tuned Decision Tree

   * Controlled depth
   * Reduced overfitting

3. Random Forest Classifier *(Final Model)*

   * Ensemble-based approach
   * Improved generalization
   * More stable predictions on unseen data

---

## Model Performance

| Model               | Train Accuracy | Test Accuracy |
| ------------------- | -------------- | ------------- |
| Decision Tree       | 1.00           | 0.70          |
| Tuned Decision Tree | 0.94           | 0.75          |
| Random Forest       | **0.97**       | **0.82**      |

**Final Model Selected:** Random Forest

Reason: Best balance between bias and variance with improved test performance.

---

## Feature Importance (Random Forest)

Approximate importance ranking:

1. DSA Level
2. CGPA
3. Number of Projects
4. Hackathon Participation
5. Tech Stack Count

This aligns well with real-world hiring expectations.

---

## Web Application

The trained model is integrated into a Flask-based web application.

### User Flow

1. User enters student profile details
2. Submits the form
3. Receives instant prediction:

   * **Shortlisted 🎉**
   * **Not Shortlisted ❌**

### Frontend

* Custom HTML and CSS (no UI frameworks)
* Clean, responsive layout
* Result-based visual feedback

### Backend

* Flask web framework
* Model loading using joblib
* Secure session handling
* POST → Redirect → GET pattern for clean UX

---

## Security & Best Practices

* No secrets hard-coded in source code
* Flask SECRET_KEY managed via environment variables
* .gitignore used to prevent committing sensitive files
* Virtual environments excluded from version control

---

## Deployment

InternSelect is deployed on Render (Free Tier).

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Data Analysis:** Pandas, NumPy
* **Machine Learning:** Scikit-learn
* **Model Persistence:** Joblib
* **Backend:** Flask
* **Frontend:** HTML, CSS
* **Deployment:** Render
* **Version Control:** Git & GitHub

---

## 📌 Project Highlights

* End-to-end machine learning pipeline
* Realistic data simulation
* Overfitting control and evaluation
* Production-ready Flask integration
* Secure cloud deployment

---

## 📈 Future Improvements

* Display prediction probability (confidence score)
* Store and visualize prediction history
* Improve dataset realism
* Integrate real-world hiring datasets
* Add authentication and user profiles

---
