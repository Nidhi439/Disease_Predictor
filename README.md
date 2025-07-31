# 🩺 Disease Prediction System using Machine Learning

This project is a simple, interactive web application that predicts diseases based on user-selected symptoms using a machine learning model. It is built using Python, Scikit-learn, Pandas, and Streamlit.

---

## 📌 Features

- Predict disease based on symptoms
- User-friendly web interface (no coding required)
- Random Forest Classifier for high accuracy
- Built with open-source tools and free to deploy

---

## 🧰 Tech Stack

| Layer | Tool |
|-------|------|
| Language | Python |
| ML Model | Scikit-learn (Random Forest Classifier) |
| Web Interface | Streamlit |
| Data Handling | Pandas, NumPy |
| Model Saving | Joblib |

---

## 📦 Requirements

Install the dependencies:

```bash
pip install -r requirements.txt
```
---

## 🏃‍♂️ How to Run the Project

After installing the requirements, follow these steps:

### ⚙️ Step 1: Clone the Repository (or download the ZIP)

```bash
git clone https://github.com/your-username/disease-predictor.git
cd disease-predictor
```

---

### 🧠 Step 2: Train the Machine Learning Model

> You only need to do this once (unless the dataset changes).

```bash
python train_model.py
```

This will:
- Train a Random Forest Classifier on the symptom–disease dataset
- Save the model (`rf_model.joblib`) and label encoder (`label_encoder.joblib`) in the `model/` folder

---

### 🖥️ Step 3: Launch the Streamlit Web App

```bash
streamlit run app.py
```

This will:
- Open a browser window
- Show a simple interface to select symptoms and predict diseases

---

### ✅ Example Usage

1. Select multiple symptoms from the dropdown.
2. Click the **"Predict Disease"** button.
3. The predicted disease will be displayed instantly.

---

## 📁 Folder Structure

```
disease-predictor/
├── dataset/
│   └── Training.csv               # Dataset with symptoms and diseases
├── model/
│   ├── rf_model.joblib            # Trained Random Forest model
│   └── label_encoder.joblib       # Saved LabelEncoder
├── app.py                         # Streamlit Web Application
├── train_model.py                 # Script to train the model
├── requirements.txt               # Dependencies
└── README.md                      # Project overview
```

---

## 🌐 Deployment (Optional)

You can deploy this app for free using [Streamlit Cloud](https://streamlit.io/cloud):

1. Push this project to a GitHub repository
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click **“Deploy an app”**
4. Connect your GitHub repo and select `app.py` as the main file
5. Streamlit will install dependencies and host your app live!

---

## 📚 Dataset Source

- [GeeksForGeeks Dataset](https://www.geeksforgeeks.org/machine-learning/disease-prediction-using-machine-learning/)
- [Download Training.csv](https://drive.google.com/file/d/1RJJcHcFXqZwDPXbzp6BqUbfACIr_burL/view)

---

## 💡 Future Improvements

- Add descriptions and precaution tips for predicted diseases
- Show probability scores for top 3 predictions
- Add chatbot or voice assistant for accessibility
- Make the layout mobile responsive

---

## 👨‍💻 Author

**Himanshu Rohilla**  
🔗 [LinkedIn](https://www.linkedin.com/in/himanshurohilla7)

---

## ⚠️ Disclaimer

This app is intended for educational and demonstration purposes only. It is **not** a substitute for professional medical advice, diagnosis, or treatment.