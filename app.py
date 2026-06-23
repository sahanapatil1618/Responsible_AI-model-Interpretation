from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("loan_model.pkl")

@app.route('/')
def home():
    return "Loan Prediction API is Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    features = np.array([[
        data['Age'],
        data['Gender'],
        data['Education'],
        data['Person Income'],
        data['Employee Experience'],
        data['Home Onwership'],
        data['Loan Amount'],
        data['Loan Intent'],
        data['Loan interest Rate'],
        data['Loan percentage'],
        data['Credit History'],
        data['Credit Score'],
        data['Previous Loan']
    ]])

    prediction = model.predict(features)[0]

    return jsonify({'Loan_Status': int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)