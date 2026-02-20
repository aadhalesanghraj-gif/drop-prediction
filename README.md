# DROP PRECDICTION
# 🎓 EduSense — AI-Powered Student Dropout Prediction


**Predict student dropout risk before it's too late — powered by Machine Learning.**


---

## 🧠 What is EduSense?

**EduSense** is an AI-powered early warning system that helps educational institutions identify students at risk of dropping out. By analyzing key academic and financial parameters, the system provides instant risk scores, department-wise distribution, and individual student explanations — enabling educators to intervene before it's too late.

> Built for hackathons. Designed for impact.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🎯 **Risk Prediction** | Instant dropout probability score for every student using CatBoost ML |
| 🔴 **Risk Classification** | Automatic categorization into High / Medium / Low Risk |
| ⭐ **Independent Performers** | Detects self-motivated students with low attendance but strong academics |
| 📊 **Smart Dashboard** | Interactive dashboard with animated charts and real-time stats |
| 🏛️ **Department Distribution** | Visual breakdown of high-risk students per department |
| 🔍 **Individual Explanation** | Click any student to see which factors are driving their risk score |
| 📂 **CSV Upload** | Drag-and-drop CSV upload with instant analysis |
| 🔎 **Filter & Search** | Filter students by risk level or search by Student ID |

---

## 🖥️ Screenshots

### 🏠 Landing Page
> Clean, professional landing page with CTA and feature highlights
> <img width="1790" height="916" alt="image" src="https://github.com/user-attachments/assets/dfeee15e-b997-47f2-ba77-c664ab5ed5a9" />


### 📤 Upload Screen
> Drag-and-drop CSV upload interface
> <img width="1300" height="500" alt="image" src="https://github.com/user-attachments/assets/6929e9f2-1d75-4cab-a433-5bb0d32d45b5" />


### 📊 Dashboard
> 5 animated stat cards → Risk distribution donut chart → Feature importance bars → Department-wise chart → Top at-risk students list
> <img width="1350" height="500" alt="image" src="https://github.com/user-attachments/assets/069341f6-fcb7-4b53-ab42-e54dd97641d9" />


### 🔍 Individual Student Explanation
> Click any student to open a detailed modal with contributing factor analysis and intervention recommendation
> <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/91995086-6bf2-4f5a-ae5b-1f5d77b3effd" />


---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **ML Model** | CatBoost Classifier |
| **Backend** | Python, Flask |
| **Frontend** | HTML, CSS, Vanilla JavaScript |
| **Data Processing** | Pandas, NumPy |


---

## 📁 Project Structure

```
drop-prediction/
│
├── Backend/
│   ├── app.py              # Flask API — routes, model loading, prediction logic
│   └── model.pkl           # Trained CatBoost model (serialized)
│
├── Frontend/
│   ├── index.html          # Complete single-file UI (CSS + JS inline)
│   ├── style.css           # (Legacy) Stylesheet
│   └── script.js           # (Legacy) JavaScript
│
├── model.ipynb             # Jupyter Notebook — data analysis, model training, evaluation
├── students_500_new.csv    # Sample dataset (500 students, 8 features)
├── requirement.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # You are here
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/drop-prediction.git
cd drop-prediction
```

### 2. Install Dependencies

```bash
pip install flask catboost pandas numpy
```

### 3. Run the App

```bash
cd Backend
python app.py
```

### 4. Open in Browser

```
http://127.0.0.1:5000
```

### 5. Upload CSV & Analyze

Upload `students_500_new.csv` (or your own dataset) and click **Run Analysis** 🎉

---

## 📋 Required CSV Columns

| Column | Description |
|--------|-------------|
| `Student_ID` | Unique student identifier |
| `Attendance` | Attendance percentage (0–100) |
| `Internal_Marks` | Internal assessment marks (0–100) |
| `Semester_Result` | Semester exam score |
| `Fee_Pending` | Outstanding fee amount |
| `LMS_Usage` | Learning Management System usage |
| `Scholarship` | Scholarship status (0 or 1) |
| `Backlogs` | Number of pending backlogs |

---

## 🤖 ML Model Details

- **Algorithm:** CatBoost Classifier (Gradient Boosting by Yandex)
- **ROC-AUC Score:** 1.0 on training data
- **Risk Thresholds:**
  - 🔴 **High Risk** → Drop Probability ≥ 60%
  - 🟡 **Medium Risk** → 40% ≤ Drop Probability < 60%
  - 🟢 **Low Risk** → Drop Probability < 40%
  - ⭐ **Independent Performer** → Low attendance + High marks + No backlogs

### Feature Importance

| Feature | Importance |
|---------|-----------|
| Backlogs | ~34.7% |
| Attendance | ~24.2% |
| Fee_Pending | ~21.0% |
| Scholarship | ~11.2% |
| Internal_Marks | ~7.7% |
| LMS_Usage | ~0.7% |
| Semester_Result | ~0.5% |

---

## 🏆 Built For

This project was built for a **hackathon** focused on AI solutions for education. It demonstrates:

- ✅ End-to-end working ML product
- ✅ Real-world explainability (not just predictions)
- ✅ Clean, professional UI built from scratch
- ✅ Solves a genuine problem in higher education

---

## 👥 Team

Built with ❤️ by students, for students.

---

