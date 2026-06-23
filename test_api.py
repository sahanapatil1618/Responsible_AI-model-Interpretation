import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "Age": 25,
    "Gender": 1,
    "Education": 0,
    "Person Income": 50000,
    "Employee Experience": 2,
    "Home Onwership": 1,
    "Loan Amount": 10000,
    "Loan Intent": 2,
    "Loan interest Rate": 12.5,
    "Loan percentage": 0.4,
    "Credit History": 3,
    "Credit Score": 650,
    "Previous Loan": 0
}

response = requests.post(url, json=data)

print("Prediction Output:")
print(response.json())