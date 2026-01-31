# Credit Card Fraud Detection – End-to-End ML Pipeline (Azure)

## 1. Project Overview
This project implements an **end-to-end credit card fraud detection pipeline** with a strong emphasis on **decision-aware machine learning**. Rather than focusing only on predictive accuracy, the project demonstrates how fraud models can be translated into **operational decision policies** that balance fraud loss, customer experience, and investigation cost.

The project covers:
- ETL using a **Medallion Architecture** (Bronze → Silver)
- Model training on **Silver-layer data**
- Evaluation under **extreme class imbalance**
- **Threshold tuning and cost-sensitive optimisation**
- Model interpretability using **feature importance and SHAP**

Dashboarding (Power BI) is intentionally **out of scope**.

---

## 2. Background and Literature Context

### 2.1 Fraud Detection as a Risk Management Problem
Credit card fraud detection is not just a classification task—it is a **risk and cost management problem**. In real financial systems:
- Fraud events are rare
- Missing fraud is significantly more expensive than false alerts
- Model value is realised only when predictions support **operational decisions**

For this reason, metrics such as **PR-AUC**, recall, and cost-sensitive evaluation are preferred over accuracy.

### 2.2 Benchmark Dataset and Prior Work
The dataset used in this project is a well-known benchmark in fraud detection research, derived from real credit card transactions. Prior studies consistently show that:
- Ensemble models outperform single classifiers
- Gradient boosting achieves strong ranking performance
- Decision thresholds must be calibrated to business costs

### 2.3 Relevance to the South African Context
Although the dataset originates from European cardholders, the modelling challenges closely mirror those faced by South African financial institutions:
- High fraud prevalence relative to transaction volume
- Strong need to balance fraud prevention with customer experience
- Limited investigation capacity

This project therefore focuses on **generalisable fraud detection principles** rather than country-specific features.

---

## 3. ETL Pipeline Architecture

### 3.1 Medallion Architecture
The pipeline follows a standard **Bronze → Silver** architecture on **Azure Data Lake Storage Gen2 (ADLS)**:

- **Bronze**: Raw ingested datasets
- **Silver**: Cleaned, validated, and analysis-ready data

Only Silver-layer data is used for modelling to ensure quality, consistency, and reproducibility.

### 3.2 Silver Dataset Description
Schema:
```
time, V1, V2, …, V28, amount, fraud_label
```

- `time`: Seconds since first transaction
- `V1–V28`: PCA-transformed behavioural features
- `amount`: Transaction value
- `fraud_label`: Binary target (1 = fraud)

Original features are unavailable due to confidentiality constraints.

---

## 4. Machine Learning Workflow

### 4.1 Data Loading
- Data loaded directly from ADLS using `adlfs` and `DefaultAzureCredential`
- No local data duplication

### 4.2 Exploratory Data Analysis
Key findings:
- Severe class imbalance (~0.17% fraud)
- Fraud is not driven solely by transaction amount
- Behavioural (PCA) features dominate predictive power

---

## 5. Model Training

### 5.1 Models Evaluated
- Decision Tree
- Random Forest
- XGBoost

### 5.2 Evaluation Metric
Primary metric: **Precision–Recall AUC (PR-AUC)**

This metric reflects model performance on the minority (fraud) class.

---

## 6. Baseline Model Performance

| Model | PR-AUC |
|------|-------|
| Decision Tree | 0.33 |
| Random Forest | 0.91 |
| **XGBoost** | **0.94** |

XGBoost was selected as the final model.

---

## 7. Threshold Tuning and Decision Calibration

Model probabilities were converted into decisions using threshold tuning.

### Evaluated Policies
- **Default (0.5)** – naive baseline
- **Precision-Constrained** – balances fraud detection and customer friction
- **Cost-Optimal** – minimises total operational cost

Cost assumptions:
```
Cost(False Negative) = 10
Cost(False Positive) = 1
```

---

## 8. Decision Policy Comparison

| Policy | Threshold | Precision | Recall | Total Cost |
|------|-----------|----------|--------|-----------|
| Default | 0.50 | 0.92 | 0.87 | 74 |
| Precision-Constrained | 0.44 | 0.91 | 0.91 | 55 |
| **Cost-Optimal** | 0.18 | 0.86 | 0.92 | **48** |

**Key Insight:** The model remains unchanged; business objectives are achieved through decision calibration.

---

## 9. Model Interpretability

### 9.1 Feature Importance
- Fraud detection is dominated by a small subset of PCA components
- Transaction amount plays a secondary but consistent role

### 9.2 SHAP Analysis
SHAP analysis shows:
- Directional influence of key behavioural components
- Non-linear and interaction effects
- Fraud decisions rely on complex patterns, not simple rules

Interpretation is performed at the **latent-pattern level**, consistent with PCA-transformed data.

---

## 10. Key Outcomes and Business Value

- PR-AUC of 0.94 demonstrates strong fraud ranking performance
- Threshold tuning reduced total operational risk by ~35%
- A single model supports multiple business policies
- Transparent decision logic supports audit and governance requirements

---

## 11. Limitations

- PCA features prevent direct business-level feature interpretation
- Cost assumptions are illustrative
- Static dataset (no concept drift analysis)

---

## 12. Technologies Used
- Python (pandas, numpy, scikit-learn, xgboost)
- SHAP
- Azure Data Lake Storage Gen2
- Azure Identity & ADLFS
- Jupyter Notebook (VS Code)

---

## 13. Status
✔ ETL complete  
✔ Model training and evaluation complete  
✔ Decision optimisation complete  
✔ Interpretability complete  
⬜ Literature expansion planned
