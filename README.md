---

### ✅ `README.md`

```

# 🏠 House Price Prediction Web App

This is a simple yet powerful machine learning web application that predicts house prices based on user input features using a trained Random Forest model. Built with **Flask**, **HTML/CSS**, and **scikit-learn**, this project is a great demonstration of end-to-end data science and deployment.

---

## 🚀 Features

- ✅ Predict house prices in real-time based on key features:
  - Overall Quality
  - Living Area (sqft)
  - Garage Cars
  - Total Basement Area (sqft)
- 📊 Visualize feature importance
- 🌐 Responsive and clean user interface
- 🔎 View insights behind the model
- 🧠 Trained using Random Forest Regressor

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (custom), Google Fonts
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, NumPy, joblib
- **Visualization**: matplotlib

---

## 📁 Project Structure

```

house-price-prediction/
│
├── app.py                      # Main Flask app
├── train\_model.py              # Script to train and save model
├── house\_price\_model.pkl       # Saved ML model
│
├── templates/
│   ├── index.html              # User input + prediction page
│   └── insights.html           # Feature importance display
│
├── static/
│   ├── feature\_importance.png  # Saved image from matplotlib
│   └── houses\_prices.jpg       # Background image for UI
│
├── train.csv                   # Dataset used for model training
├── README.md                   # You're here!

````

---

## 📊 How the Model Works

The model uses the following features:

- `OverallQual` - Overall material and finish quality
- `GrLivArea` - Above ground living area (sqft)
- `GarageCars` - Number of cars that can fit in the garage
- `TotalBsmtSF` - Total basement area (sqft)

It was trained using **RandomForestRegressor** and saved using `joblib`.

---

## 🖼️ Screenshots

![image](https://github.com/user-attachments/assets/e2505aea-8fe8-494e-91e5-618bde4ef51a)


**Feature Importance**  
![image](https://github.com/user-attachments/assets/72262a59-7d27-4e23-9a05-ceda09b2d39c)


---

## ▶️ How to Run

1. **Install dependencies**

```bash
pip install flask pandas numpy scikit-learn matplotlib joblib
````

2. **Train the model** (optional)

```bash
python train_model.py
```

3. **Run the Flask app**

```bash
python app.py
```

4. Open in your browser:
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 💡 Ideas to Enhance

* Add more input features from the dataset
* Use a different ML model or implement model comparison
* Add interactive charts (e.g. plotly/d3.js)
* Connect to a database for logging predictions

---

## 📚 Dataset Source

* [Ames Housing Dataset](https://www.kaggle.com/datasets/prevek18/house-price-prediction-dataset)

---

## 📩 Contact

👨‍💻 **Author**: *Tushar Wankhede*
📧 *wankhedetushar9@gmail.com*

---

## ⭐ If you found this project useful, feel free to star the repo!

```
