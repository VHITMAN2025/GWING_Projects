# 🩺 Diabetes Prediction Web App

Welcome to the **Diabetes Prediction Web App**!  
This project uses machine learning to predict whether a patient is diabetic or non-diabetic based on medical details. It features a beautiful web interface, generates professional PDF medical reports, and is perfect for clinics, diagnostics centers, or educational demos.

---

## 🚀 Features

- **Modern Web Interface:** Responsive, user-friendly form for patient data entry.
- **Machine Learning Powered:** Uses SVM for accurate diabetes prediction.
- **Instant Results:** Get prediction instantly after submitting patient details.
- **Professional PDF Reports:** Download a stylish, branded medical report with doctor’s signature.
- **Attractive Design:** Custom branding for "Vijay Diagnostics" and Dr. Vijay.
- **Easy Deployment:** Ready to run locally or deploy on cloud platforms.

---

## 🖼️ Screenshots

![Form Screenshot](screenshots/form.png)
![Result Screenshot](screenshots/result.png)
![PDF Report Screenshot](screenshots/pdf_report.png)

---

## 🏗️ How It Works

1. **Enter Patient Details:** Fill out the form with medical information.
2. **Predict:** The app uses a trained SVM model to predict diabetes.
3. **View Result:** Instantly see if the patient is diabetic or not.
4. **Download Report:** Get a professional PDF report with all details and prediction.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS (responsive, modern design)
- **Backend:** Python, Flask
- **ML Model:** scikit-learn (SVM)
- **PDF Generation:** FPDF
- **Data:** [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

---

## ⚡ Quick Start

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/diabetes-prediction-app.git
    cd diabetes-prediction-app
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Train the model (if needed):**
    - Run `diabetes_prediction.ipynb` to train and save `model.pkl`.

4. **Run the app:**
    ```bash
    python app.py
    ```

5. **Open in browser:**
    - Go to [http://localhost:5000](http://localhost:5000)

---

## 📄 PDF Report Sample

- Branded with "Vijay Diagnostics" and Dr. Vijay
- Patient details, prediction result, and doctor’s signature
- Professional, print-ready format

---

## 📂 Project Structure

```
├── app.py
├── diabetes_prediction.ipynb
├── diabetes.csv
├── model.pkl
├── static/
│   └── signature.png
├── templates/
│   ├── form.html
│   ├── diabetic.html
│   └── nondiabetic.html
└── requirements.txt
```

---

## 🙌 Credits

- Inspired by the [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- Developed by [Your Name] for Vijay Diagnostics

---

## 📢 License

This project is licensed under the MIT License.

---

**Give it a ⭐ if you like it! Contributions and suggestions are welcome.**
