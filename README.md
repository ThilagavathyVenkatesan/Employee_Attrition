# 🚀 Employee Attrition Analysis & Prediction

This project analyzes employee attrition using **machine learning models** and provides an **interactive Streamlit dashboard** for HR insights.  
It helps organizations identify key factors leading to attrition and predict the risk of employees leaving.

---

## 📊 Project Overview

- Exploratory Data Analysis (EDA) on employee dataset
- Outlier detection & feature importance
- Machine Learning models for attrition prediction
- Model performance comparison (Accuracy, Precision, Recall, F1, AUC-ROC)
- Interactive Streamlit Dashboard:
  - 📌 Home Dashboard → View insights (high-risk employees, high satisfaction, performance scores)
  - 📌 Prediction Page → Enter employee details to predict attrition risk

---

## 📂 Dataset

- **Employee-Attrition.csv**  
  Contains employee demographic, job-related, and performance data.  
  *(The dataset used is a sample HR dataset with 1470 rows and 35 columns.)*

---

## 🛠️ Tech Stack

- **Python**: Pandas, NumPy, Matplotlib, Seaborn  
- **Machine Learning**: scikit-learn (Random Forest, Gradient Boost, Decision Tree, Logistic Regression)  
- **Dashboard**: Streamlit  
- **Model Persistence**: Pickle  
- **Visualization**: PowerPoint & Streamlit plots  

---

## 📑 Project Structure

```
Employee_Attrition
│
├── app.py                  # Streamlit Dashboard
├── train_model.py          # Model training script
├── best_model.pkl          # Saved ML model
├── Employee-Attrition.csv  # Dataset
├── employeeeda.ipynb       # Notebook for EDA
├── employeeml.ipynb        # Notebook for ML models
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── /images                 # Screenshots for README
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
   git clone https://github.com/ThilagavathyVenkatesan/Employee_Attrition.git
   cd Employee_Attrition
```


### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Jupyter Notebooks

```bash
jupyter notebook
```
Open employeeeda.ipynb → For Exploratory Data Analysis
Open employeeml.ipynb → For Model Training & Evaluation

### 4. Train the model

```bash
python train_model.py
```
This will save the best model as best_model.pkl.


### 5. Run the Streamlit Dashboard

```bash
streamlit run empapp.py
```
