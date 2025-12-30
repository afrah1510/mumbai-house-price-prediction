# House Price Prediction using Machine Learning

## Abstract

Machine learning algorithms are increasingly being used for the **mass appraisal of real estate** and in **automated valuation models (AVMs)** to help users make informed decisions.  
This project aims to develop a **predictive model for house prices in Mumbai** using machine learning algorithms, while also **analyzing the impact of the COVID-19 pandemic** on property values.

The model considers several influential factors such as:
- Location  
- Plot size  
- Zoning regulations  
- Accessibility to transportation  
- Crime rates  
- Demographic trends  

According to **Anarock Research**, there has been a **13% increase in the average property prices** across the Mumbai Metropolitan Region (MMR).  
Our predictive model is based on **Random Forest Regression**, a robust statistical method for predictive analysis.  

This project will benefit:
- Real estate professionals  
- Landowners  
- Developers  
- Investors  
- Businesspersons  

by providing insights and data-driven estimates to guide property buying and selling decisions.

---

## Problem Statement

We aim to develop a **machine learning application** capable of **predicting land prices** based on multiple parameters, including:
- Pricing  
- Location  
- Availability of basic amenities  
- Neighborhood economic value  

The target users include:
- Common people  
- Developers  
- Investors  
- Industrialists  
- Businesspersons  

---

## System Requirements

### Software Requirements
| Component | Specification |
|------------|----------------|
| **Operating System** | Windows 10 or higher |
| **Programming Language** | Python |
| **IDE / Development Tools** | Jupyter Notebook, Google Colab |
| **Web Framework** | Flask |

### Hardware Requirements
| Component | Minimum Requirement |
|------------|---------------------|
| **Processor** | Intel Core i3, 5th Gen or newer |
| **Hard Disk** | 1 GB free space |
| **RAM** | 4 GB |

---

## Technologies Used

- **Python**   
- **Flask** (for web integration)  
- **Scikit-learn** (machine learning)  
- **Pandas & NumPy** (data processing)  
- **Matplotlib / Seaborn** (visualization)  
- **Jupyter Notebook / Google Colab** (development environment)

---

## Features

- Predict land prices based on multiple influencing factors
- Analyze COVID-19’s impact on Mumbai’s real estate prices
- Visualize property price trends using data analytics
- Simple web interface for user interaction
- Model built using Decision Tree Regression  

---

## Workflow

1. **Data Collection** – Collect real estate data (location, area, price, amenities, etc.)  
2. **Data Preprocessing** – Handle missing values, normalization, and encoding  
3. **Feature Selection** – Identify the most impactful attributes  
4. **Model Training** – Apply Decision Tree Regression algorithm  
5. **Evaluation** – Test model accuracy using performance metrics  
6. **Deployment** – Host the model using Flask  

---

## How to Run the Project

**1. Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/mumbai-house-price-prediction.git
   cd land-price-prediction
   ```

**2. Install dependencies**
  ```bash
  pip install -r requirements.txt
  ```

**3. Run Jupyter Notebook**
   ```bash
   jupyter notebook
   ```
   or open the project in Google Colab.

**5. Launch the Flask App**
  ```bash
  python app.py
  ```
  Open the app in your browser at
  http://127.0.0.1:5000/
