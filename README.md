# Heart Disease Predictor 🫀

This Streamlit app predicts the likelihood of heart disease using a machine learning model trained on medical features. Users can input key health indicators, and the model will estimate the risk of heart disease.


## 📂 Project Structure

- `heart_disease.py` — Streamlit app script  
- `saved model/heart_disease_model.sav` — Trained machine learning model (pickled)  
- `requirements.txt` — List of Python dependencies  
- `heart_disease_train.csv` — Dataset   
- `Group_Project.ipynb` — Notebook for model development  
- `Report.pdf`  - Project Report


## 🚀 How to Run Locally

# 1️⃣ Clone the repository
```bash
git clone https://github.com/zooviee/heart-disease-predictor.git
cd heart-disease-predictor
```


# 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

# 3️⃣ Run the Streamlit app
```bash
streamlit run heart_disease.py
```

## 🌐 Live App (Streamlit Cloud)
you can access the app at:
👉 https://zooviee-heart-disease-predictor-heart-disease-shd9pt.streamlit.app/


## 🏥 Features

✅ User inputs:
- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure 
- Cholesterol 
- ECG results
- Max Heart Rate
- Exercise Angina 
- Oldpeak
- Slope

✅ Instant ML-based risk prediction
✅ User guidance with input ranges for precise predictions


## ⚠ Notes

The .sav model file is required for predictions.
Ensure the input format matches the expected model features.

## 📜 License

This project is for educational and research purposes.


## ✨ Contributors

Oluwaseyi Akinsanya (@zooviee)

