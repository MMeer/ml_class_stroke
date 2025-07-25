# Stroke Prediction Dataset for Insurance Premium Modeling

## Business Case Overview

This dataset enables insurance companies to develop sophisticated risk assessment models for stroke prediction, allowing for more accurate premium pricing based on individual risk profiles. By leveraging machine learning techniques on clinical features, insurers can make data-driven decisions about premium rates while maintaining competitive pricing strategies.

## Dataset Information

- **Source**: [Kaggle - Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- **Size**: 5,110 records with 12 attributes
- **Target Variable**: stroke (binary: 1 if stroke occurred, 0 otherwise)
- **File Format**: CSV (healthcare-dataset-stroke-data.csv)

## Features Description

### Demographic Features

- **id**: Unique identifier for each patient
- **gender**: Patient gender (Male/Female/Other)
- **age**: Patient age in years
- **hypertension**: History of hypertension (0: No, 1: Yes)
- **heart_disease**: History of heart disease (0: No, 1: Yes)
- **ever_married**: Marital status (Yes/No)
- **Residence_type**: Type of residence (Urban/Rural)

### Lifestyle & Health Features

- **work_type**: Employment category (Private, Self-employed, Govt_job, children, Never_worked)
- **smoking_status**: Smoking history (formerly smoked, never smoked, smokes, Unknown)
- **avg_glucose_level**: Average glucose level in blood
- **bmi**: Body Mass Index

### Target Variable

- **stroke**: Stroke occurrence (1: Yes, 0: No)

## Insurance Business Applications

### 1. Risk Stratification

- **Low Risk**: Young, non-smokers with normal BMI and glucose levels
- **Medium Risk**: Middle-aged with one or two risk factors
- **High Risk**: Elderly with multiple comorbidities (hypertension, heart disease, high glucose)

### 2. Premium Calculation Framework

```
Base Premium × Risk Multiplier = Final Premium

Risk Multipliers (Example):
- Age > 65: 1.5x
- Hypertension: 1.3x
- Heart Disease: 1.4x
- Smoking: 1.6x
- High BMI (>30): 1.2x
- High Glucose (>200): 1.3x
```

### 3. Actuarial Insights

- **Most Predictive Features**: Age, hypertension, heart disease, glucose levels
- **Stroke Rate**:
- **Gender Patterns**: Analyze differential risk by gender
- **Geographic Factors**: Urban vs Rural residence impact

## Data Quality Considerations

### Missing Values

- **BMI**: Contains missing values that require imputation
- **Smoking Status**: Some records marked as "Unknown"

### Class Imbalance

- **stroke**: The dataset is highly imbalanced. Out of 5,110 patients, only 249 have experienced a stroke (~5%).

### Data Preprocessing Requirements

1. **Categorical Encoding**: Convert categorical variables to numerical
2. **Missing Value Imputation**: Handle BMI and other missing values
3. **Feature Scaling**: Normalize numerical features
4. **Outlier Detection**:

## Model Development Strategy

### 1. Exploratory Data Analysis

- Correlation analysis between features
- Distribution analysis of stroke cases by demographic groups
- Risk factor prevalence analysis
- correlation analysis between pre-menopausal and post menopuasal women and stroke risk

### 2. Feature Engineering

- Age groups (18-30, 31-50, 51-65, 65+)
- BMI categories (Underweight, Normal, Overweight, Obese)
- Glucose level categories (Normal, Pre-diabetic, Diabetic)
- Composite risk scores

### 3. Model Selection

- **Logistic Regression**: Interpretable baseline model
- **Random Forest**: Handle non-linear relationships
- **XGBoost**: High performance with feature importance
- **Neural Networks**: Complex pattern recognition

### 4. Evaluation Metrics

- **Precision**: Minimize false positives (over-charging low-risk customers)
- **Recall**: Identify high-risk individuals (avoid under-charging)
- **F1-Score**: Balance between precision and recall
-

## Implementation Guidelines

### Model Training

```python- version ....
# Example workflow
1. Data loading and cleaning
2. Feature engineering
3. Train-test split (80-20)
4. Handle class imbalance
5. Model training with cross-validation
6. Hyperparameter tuning
7. Model evaluation and selection
```

### Installation Steps

- pip install -r requirements

### To launch FastAPI application for end point prediction to be invoked from Web/UI

- uvicorn main:app -reload

### Production Deployment

- **Real-time Scoring**: API for premium calculation
- **Batch Processing**: Periodic risk assessment updates
- **Model Monitoring**: Track model performance over time
- **Regulatory Compliance**: Ensure fair pricing practices

## Ethical Considerations

### Fairness and Bias

- Ensure no discrimination based on protected characteristics
- Regular bias audits across demographic groups
- Transparent risk factor communication to customers

### Regulatory Compliance

- Adherence to insurance regulations in target markets
- Documentation of risk assessment methodology
- Regular model validation and updates

### Data Privacy

- Secure handling of personal health information
- Compliance with HIPAA/GDPR requirements
- Anonymization of sensitive data

## Business Value Proposition

### For Insurance Companies

- **Improved Risk Assessment**: More accurate pricing reduces losses
- **Competitive Advantage**: Better risk selection
- **Regulatory Compliance**: Data-driven premium justification
- **Customer Retention**: Fair pricing based on individual risk

### For Customers

- **Personalized Pricing**: Pay premiums based on actual risk
- **Health Incentives**: Lower premiums for healthy lifestyle choices
- **Transparency**: Clear understanding of risk factors

## Next Steps

1. **Data Acquisition**: Obtain the dataset from Kaggle
2. **Team Setup**: Assemble the team and allocate targeted prolems to work with based on expertise
3. **Regulatory Review**: Ensure compliance with insurance regulations

## Technical Requirements

### Software Stack

- **Python 3.8+**: Primary development language
- **Pandas/NumPy**: Data manipulation
- **Scikit-learn**: Machine learning models
- **XGBoost**: Advanced algorithms
- **MLflow**: Model tracking and deployment
- **Docker**: Containerization for deployment

### Infrastructure

## Contact Information

For questions about implementation or model development, contact:

- Amir : [email]
- Kevin : nageswarkv@gmail.com
- Lakshmi : [email]
- Markus :[email]
- Meer : [email]

---

**Disclaimer**: This dataset and models are for educational and research purposes. Always consult with legal and regulatory experts before implementing risk assessment models in production insurance systems.
