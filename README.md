# ❤️ Heart Disease Prediction Project

A complete Machine Learning project to **predict the presence of heart disease** using the [Kaggle Heart Disease Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction). This project includes **data cleaning, preprocessing, exploratory data analysis, feature selection, modeling, evaluation, and deployment** through a Flask web application.  

---

## **Video Demonstration**

📹 Demo of the app and workflow:

![Watch Demo Video ](screenshots/demo.mp4)

*(Click the thumbnail to play video or open `videos/demo.mp4` locally.)*

---

## **Project Motivation**

Heart disease is one of the leading causes of death globally. Early prediction helps identify high-risk patients and can potentially save lives. This project demonstrates the full workflow from **raw data to a predictive web app**, making it an end-to-end example of a real-world ML project.

---

## **Project Workflow**

1. **Data Exploration & Cleaning**
   - Analyzed missing values and inconsistencies.  
   - Explored feature distributions and relationships.  
   - Encoded categorical features and scaled numeric features.  
   - Notebooks: [Heart Cleaning & EDA](notebooks/heart-eda-cleaning.ipynb)

2. **Feature Engineering**
   - Used **Random Forest** to determine the most important features.  
   - Created a reduced dataset with only the top predictive features.

3. **Modeling**
   - Built a **pipeline** with preprocessing + **XGBoost** classifier.  
   - Train/Test Accuracy:
     - Train Accuracy: 86%  
     - Test Accuracy: 84%  
   - Plotted a **correlation heatmap** of processed features.

4. **Visualization**
   - Explored relationships between features and target variable.
   - Generated key plots to gain insights.  
   - Saved visualizations in `screenshots/` folder.

5. **Deployment**
   - Built a **Flask web application** for user input.  
   - Integrated preprocessing and trained model.  
   - Users can input patient data and get a real-time heart disease prediction.  
   - Screenshots and video demonstration included below.

---

## **Repository Structure**
```
heart-disease-project/
│
├─-- dataset/                                         # Original and processed datasets
├─-- notebooks/                                       # Jupyter notebooks for EDA and modeling
├─-- src/                                             # Python scripts for preprocessing, feature selection
├─-- models/                                          # Trained XGBoost model files (pipe.pkl)
├─-- ds_plots/                                        # Plots Images 
├─-- templates/                                       # HTML files
├─-- static/                                          # Image files
├─-- app.py                                           # Flask code
├─-- screenshots/                                     # Screenshots and demo video
├─ requirements.txt                                   # Python dependencies
├─ README.md                                          # Project documentation
└─ .gitignore                                         # Files/folders to ignore in Git 

```



---

## **Visualizations**

### **1. Correlation Heatmap**
![Correlation Heatmap](ds_plots/correlation.png)

### **2. Feature Importance**
![Feature Importance](ds_plots/feature_importance.png)

### **3. Heart Risk Increase With ST Slope Change**
![ST Slope - Heart Disease](ds_plots/heart_risk_inc_st_slope.png)

### **4. Distribution of Age vs Heart Disease**
![Age vs Heart Disease](ds_plots/age.png)

### **5. Cholesterol vs Max Heart Rate**
![Cholesterol](ds_plots/cholesterol.png)
![MaxHR](ds_plots/max_heart_rate.png)


---

## **Web Application Screenshots**

### **Home Page**
![App Home](screenshots/home_page.png)
![App Home](screenshots/home_page2.png)

### **User Input Form**
![App Input Form](screenshots/form_fill.png)
![App Input Form](screenshots/form_fill1.png)

### **Prediction Result**
![App Result](screenshots/result.png)

---


## **Notebooks & Code**

### **Notebooks**
- [Data Cleaning & EDA](notebooks/heart-eda-cleaning.ipynb)  
- [Feature Selection & Modeling](notebooks/heart-model.ipynb)  

### **Source Code**
- [Flask App](app.py)  
- [HTML Templates](templates/index.html)  
- [CSS / Static Files](static/style.css)  
- Optional scripts (if refactored):
  - [Preprocessing](src/preprocessing.py)
  - [Feature Selection](src/feature_selection.py)
  - [Model Training](src/model_training.py)

### **Models** 
- Preprocessing Trained pipeline: `models/pipe.pkl`

---

## **Installation & Usage**

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/heart-disease-project.git
cd heart-disease-project
