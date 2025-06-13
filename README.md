# 🌾 Crop Recommendation System

A lightweight machine learning-powered web application that recommends the most suitable crop to cultivate based on soil nutrient values (N, P, K) and pH. This system uses Logistic Regression and Random Forest models and provides highly accurate crop recommendations tailored perfectly for your soil conditions.

---

## 🔍 Features

- 🌿 Recommends crops based on soil nutrients and pH
- ⚙️ Choose between Logistic Regression and Random Forest models
- 🌍 Simple, responsive frontend using HTML, CSS, and JavaScript
- 🚀 Backend built with Flask and integrated with CORS

---

## 🧪 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask, Flask-CORS
- **ML Models:** Logistic Regression, Random Forest (Scikit-learn)
- **Data Handling:** Pandas
- **Model Persistence:** Joblib

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/VISHNUARAVIND17/crop-recommendation-system.git
cd crop-recommendation-system
```


### 2. Set Up a Virtual Environment (Recommended)

Create and activate a virtual environment to isolate your project dependencies:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Necessary Libraries

Install dependencies in the virtual environment:

```bash
pip install -r requirements.txt
```

### 4. Start the Flask server:

```bash
python backend/app.py
```

### 5. Open the Frontend

Open the file `frontend/index.html` in your browser.

Alternatively, you can run it through XAMPP or any local server.

---

## 🌱 Usage

1. Enter values for Nitrogen (N), Phosphorus (P), Potassium (K), and pH.
2. Choose the model: Logistic Regression or Random Forest.
3. Click “Recommend Crop”.
4. Get the crop recommended for your soil type.

---

## 🧠 Models

### 🔹 Logistic Regression
A simple and fast classification algorithm that learns a straight-line decision boundary to separate different crop classes based on soil nutrients and pH.

### 🔹 Random Forest
A robust ensemble method that builds multiple decision trees on random subsets of data and aggregates their outputs.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## ✨ Author

Made with ❤️ by Vishnu Aravind