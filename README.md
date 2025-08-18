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
└── Screenshots             # Screenshots for README
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
⭕Open employeeeda.ipynb → For Exploratory Data Analysis                                                                                                                                   
⭕Open employeeml.ipynb → For Model Training & Evaluation

### 4. Train the model

```bash
python train_model.py
```
This will save the best model as best_model.pkl.


### 5. Run the Streamlit Dashboard

```bash
streamlit run empapp.py
```


## 📸 Screenshots
<img width="1366" height="768" alt="Screenshot (46)" src="https://github.com/user-attachments/assets/e87950cd-13b1-4026-baa9-5023fbff963d" />
<img width="1366" height="768" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/37348206-78f1-4bb8-bbba-42947ea4efa2" />
<img width="1366" height="768" alt="Screenshot (48)" src="https://github.com/user-attachments/assets/38e087d5-c48b-4500-96fa-f146933de6f6" />
<img width="1366" height="768" alt="Screenshot (49)" src="https://github.com/user-attachments/assets/59965fb6-e526-4644-89aa-0173c5eb0bc3" />
<img width="1366" height="768" alt="Screenshot (50)" src="https://github.com/user-attachments/assets/9a53b4d3-7e91-415b-bb05-a928abeb9098" />
<img width="1366" height="768" alt="Screenshot (51)" src="https://github.com/user-attachments/assets/703d81f6-5ece-4328-a9fe-726d3e9f8653" />
<img width="1366" height="768" alt="Screenshot (52)" src="https://github.com/user-attachments/assets/bb9d6df4-d6ed-400e-aeee-666eb8ad12e4" />
<img width="1366" height="768" alt="Screenshot (53)" src="https://github.com/user-attachments/assets/e0e51e43-bf31-4ff5-97c6-32bc8a0ab6c5" />
<img width="1366" height="768" alt="Screenshot (54)" src="https://github.com/user-attachments/assets/8a0faee7-8620-4c7f-b419-7a3a7b753ce1" />
<img width="1366" height="768" alt="Screenshot (55)" src="https://github.com/user-attachments/assets/859a71ed-e782-4ec4-a88c-2898cdbe161d" />
<img width="1366" height="768" alt="Screenshot (56)" src="https://github.com/user-attachments/assets/24c08420-b86f-4ef7-b707-a0ea7fcd7ad3" />
<img width="1366" height="768" alt="Screenshot (57)" src="https://github.com/user-attachments/assets/9c83e25e-3bcb-41c8-b9bd-6a550ce1c2b4" />












