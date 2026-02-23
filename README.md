# 🤖 AI/ML Projects — Anisha

> A collection of hands-on Artificial Intelligence and Machine Learning projects covering data analysis, visualization, and interactive dashboards.

---

## 📁 Project 1 — Student Performance Analysis & Dashboard

### 📌 Overview
An end-to-end data analysis project that explores factors affecting student academic performance. The project includes data preprocessing, exploratory data analysis (EDA), and an interactive Streamlit dashboard for visual insights.

### 📂 Files
| File | Description |
|------|-------------|
| `Project_1.py` / `Project_1.ipynb` | Full analysis pipeline + Streamlit dashboard code |
| `Student_Performance_Dashboard.html` | Exported dashboard view |
| `student_dataset.csv` | Dataset used for analysis |

### 🧰 Tech Stack
- **Python** — Core language
- **Pandas & NumPy** — Data manipulation
- **Matplotlib & Seaborn** — Data visualization
- **Streamlit** — Interactive dashboard

### 🔍 What the Project Covers

**1. Data Exploration**
- Loaded and inspected the student dataset (300 records)
- Checked for missing values and duplicate entries
- Explored data types and feature distributions

**2. Outlier Detection & Removal**
- Used boxplots to visually identify outliers in numerical columns
- Confirmed and removed outliers in `final_exam_marks` using the IQR method
- Reduced dataset from 300 → 299 rows after removal

**3. Feature Engineering — Categorical Encoding**
- Applied **One-Hot Encoding** on nominal columns: `gender`, `internet_access`, `extracurricular`
- Applied **Manual Label Encoding** on ordinal column: `family_income` (Low=0, Medium=1, High=2)

**4. Exploratory Data Analysis (EDA)**
- Correlation heatmap to identify relationships between features
- Distribution plot of the target variable `final_exam_marks`
- Scatter plots: Study Hours vs Marks, Attendance vs Marks
- Box plots: Gender vs Marks, Family Income vs Marks

**5. Interactive Streamlit Dashboard**
- Filter students by study hours range using a sidebar slider
- Live KPIs: Total Students, Average Marks, Highest Marks
- Scatter plot: Study Hours vs Final Marks (color-coded)
- Histogram with KDE: Distribution of Final Marks
- Full Correlation Heatmap

### 💡 Key Insights
- Students who study more hours consistently score higher marks
- Positive correlation exists between study hours and final exam performance
- Marks distribution is moderately spread with few high performers
- Family income level shows a noticeable influence on academic outcomes

### ▶️ How to Run

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn streamlit

# Run the dashboard
streamlit run Project_1.py
```

---

## 🛠️ Setup & Requirements

```bash
pip install pandas numpy matplotlib seaborn streamlit
```

| Library | Version (recommended) |
|---------|----------------------|
| pandas | ≥ 1.5 |
| numpy | ≥ 1.23 |
| matplotlib | ≥ 3.6 |
| seaborn | ≥ 0.12 |
| streamlit | ≥ 1.20 |

---

## 👩‍💻 Author

**Anisha**
- GitHub: [@anisha-1811](https://github.com/anisha-1811)

---

## 📄 License

This repository is for educational and portfolio purposes.

---

> ⭐ If you found this helpful, consider starring the repository!
