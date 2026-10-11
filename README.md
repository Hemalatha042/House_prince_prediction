# 🏠 House Price Prediction

**An end-to-end Machine Learning project with an interactive Streamlit application.**

Predict house prices by entering property details such as area, number of bedrooms, bathrooms, age, and location rating.

## ✨ Project Highlights

- 📊 Explored and analyzed housing data.
- 🤖 Trained two regression models: Linear Regression and Random Forest.
- 📈 Evaluated models using MAE, MSE, and R².
- 🏡 Built a web app for predicting prices of new houses.
- 💾 Saved the trained model for reuse without retraining.

## 🛠️ Tech Stack

| Tool         |    Purpose      |
|------------  |-----------------|
| Python       | Programming     |
| Pandas       | Data handling   |
| Scikit-learn | Machine Learning |
| Streamlit    | Web application   |
| Joblib       | Model persistence |
| Matplotlib   | Data visualization |

## 📥 Property Details

The model accepts five inputs:

- **Bedrooms** — number of bedrooms
- **Bathrooms** — number of bathrooms
- **Square Feet** — property area
- **House Age** — age of the property
- **Location Rating** — numerical rating of the location

## 🧠 Models & Evaluation

Two regression algorithms were evaluated on the same train-test split.

| Model | Test R² |
|---|---:|
| Linear Regression | 1.0000 |
| Random Forest Regressor | 0.9999 |

Linear Regression performed best on this dataset, with near-zero prediction error.

> **Data limitation:** The dataset appears to follow a synthetic pricing pattern in which square footage strongly determines the price. These results demonstrate the workflow, not real-world housing-market accuracy.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd house-price-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the application

```bash
python -m streamlit run notebook/app.py
```

Enter the property details and click **Predict Price** to view the model's estimate.

## 📂 Project Structure

```text
house_price_prediction/
├── data/                # Housing dataset
├── notebook/            # Model and Streamlit app
│   ├── app.py
│   └── house_price_model.pkl
├── README.md
├── requirements.txt
└── .gitignore
```

## 🎯 Learning Outcomes

- Data exploration and preparation
- Regression model training
- Model evaluation and comparison
- Making predictions on new data
- Integrating a saved ML model into a web app

## 👩‍💻 About

This project was developed as a hands-on exercise in Machine Learning and application development, combining model training with a simple, interactive user interface.

**Future improvement:** Evaluate the workflow using a real-world housing dataset with more realistic property and location features.