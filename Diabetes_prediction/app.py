from flask import Flask, render_template, request, redirect, url_for, send_file, session
import pickle
import numpy as np
import io
import os
from fpdf import FPDF
from datetime import datetime
# from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
app.secret_key = os.urandom(24)
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    data = [
        float(request.form['pregnancies']),
        float(request.form['glucose']),
        float(request.form['bp']),
        float(request.form['skin']),
        float(request.form['insulin']),
        float(request.form['bmi']),
        float(request.form['dpf']),
        float(request.form['age'])
    ]
    # prediction = model.predict([data])

    ########## Data Preprocessing and Model Implementation
    input_data = np.asarray(data).reshape(1,-1)
    print("Input Data:",input_data)

    std_data = scaler.transform(input_data)

    outcome_prediction = model.predict(std_data)
    print("The prediction:",outcome_prediction)

    if outcome_prediction[0] == 1:
       print("Patient is Diabetic")
    else:
       print("Patient is Non - Diabetic")
    ###############
    
    result = "Diabetic" if outcome_prediction[0] == 1 else "Non-Diabetic"
    session['report'] = {
        'name': name,
        'pregnancies': data[0],
        'glucose': data[1],
        'bp': data[2],
        'skin': data[3],
        'insulin': data[4],
        'bmi': data[5],
        'dpf': data[6],
        'age': data[7],
        'result': result
    }
    if outcome_prediction[0] == 1:
        return redirect(url_for('diabetic'))
    else:
        return redirect(url_for('nondiabetic'))

@app.route('/nondiabetic')
def nondiabetic():
    return render_template('nondiabetic.html')

@app.route('/diabetic')
def diabetic():
    return render_template('diabetic.html')

@app.route('/download_report')
def download_report():
    report = session.get('report')
    if not report:
        return "No report available.", 400
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(34, 139, 230)
    pdf.rect(0, 0, 210, 25, 'F')
    pdf.set_xy(0, 8)
    pdf.set_font("Arial", 'B', 22)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(210, 10, "Vijay Diagnostics", ln=True, align='C')
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Medical Report", ln=True, align='C')
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, f"Patient Name: {report['name']}", ln=True)
    pdf.cell(0, 8, f"Age: {report['age']}", ln=True)
    pdf.cell(0, 8, f"Date: {datetime.now().strftime('%d-%m-%Y')}", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_fill_color(230, 240, 255)
    pdf.cell(80, 10, "Parameter", 1, 0, 'C', True)
    pdf.cell(60, 10, "Value", 1, 1, 'C', True)
    pdf.set_font("Arial", '', 12)
    row_fill = False
    for label, value in [
        ("Pregnancies", report['pregnancies']),
        ("Glucose Level", report['glucose']),
        ("Blood Pressure", report['bp']),
        ("Skin Thickness", report['skin']),
        ("Insulin", report['insulin']),
        ("BMI", report['bmi']),
        ("Diabetes Pedigree Function", report['dpf']),
    ]:
        pdf.set_fill_color(245, 250, 255) if row_fill else pdf.set_fill_color(255, 255, 255)
        pdf.cell(80, 10, label, 1, 0, 'L', True)
        pdf.cell(60, 10, str(value), 1, 1, 'C', True)
        row_fill = not row_fill
    pdf.ln(8)
    if report['result'] == "Diabetic":
        pdf.set_fill_color(255, 80, 80)
        pdf.set_text_color(255, 255, 255)
        result_text = "DIABETIC"
    else:
        pdf.set_fill_color(34, 200, 100)
        pdf.set_text_color(255, 255, 255)
        result_text = "NON-DIABETIC"
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 18, result_text, ln=True, align='C', fill=True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    pdf.set_draw_color(180, 180, 180)
    pdf.set_line_width(0.5)
    pdf.line(140, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(2)
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(0, 8, "Dr. Vijay", ln=True, align='R')
    pdf.cell(0, 8, "Vijay Diagnostics", ln=True, align='R')
    y_signature = pdf.get_y()
    x_signature = 210 - 40 - 10
    try:
        pdf.image("static/signature.png", x=x_signature, y=y_signature, w=40)
    except RuntimeError:
        pass
    pdf.ln(22)
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    buffer = io.BytesIO(pdf_bytes)
    filename = f"{report['name'].replace(' ', '_')}_medical_report.pdf"
    return send_file(
        buffer,
        as_attachment=True,
        download_name=filename,
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)
