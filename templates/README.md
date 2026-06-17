# Fertilizer Recommendation System

## Project Overview
This project focuses on improving fertilizer decision-making in agriculture by analyzing soil nutrients, environmental conditions, and crop types. The goal is to support better agricultural decisions by identifying patterns that link soil and crop characteristics to appropriate fertilizer types.

The system is built using a structured agricultural dataset and includes exploratory data analysis, feature engineering, and a machine learning-based recommendation model.

---

##  Dataset Description
The dataset contains soil, crop, and environmental variables including:

- Temperature
- Humidity
- Moisture
- Soil Type
- Crop Type
- Nitrogen
- Phosphorus
- Potassium
- Fertilizer Name (Target Variable)

---

##  Workflow

1. Data Cleaning and Quality Check  
2. Exploratory Data Analysis (EDA)  
3. Feature Engineering  
4. Model Building (Random Forest Classifier)  
5. Evaluation and Insights Generation  

---

##  Feature Engineering

New features were created to improve model understanding:

- **NPK Score**: Overall soil fertility level  
- **Water Saturation**: Combination of soil moisture and humidity  
- **Environmental Index**: Interaction between temperature and humidity   

These features help capture hidden agricultural relationships in the data.

---

##  Model Used

A **Random Forest Classifier** was used for fertilizer prediction because it:
- Handles both numerical and categorical data well  
- Captures non-linear relationships  
- Reduces overfitting using ensemble learning  

The model predicts the most suitable fertilizer based on soil and environmental conditions.

---

##  Key Insights

- Fertilizer selection is strongly influenced by crop type and soil type  
- Nutrient levels (N, P, K) play a major role in recommendations  
- Data shows stable distributions with no significant outliers  
- Features are mostly independent with low correlation  

---

##  Tech Stack

- Python  
- Pandas & NumPy  
- Scikit-learn  
- Seaborn & Matplotlib  

---

##  Future Improvements

- Deployment using Streamlit or Flask  
- Integration with real-time soil sensors  
- Advanced ensemble or boosting models  
- Mobile-friendly farmer advisory system  

---

## Author
Developed By Akimu Odunola as part of a Data Science Internship Assessment at RHEA focused on agricultural decision support systems.