# app.py
from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('best_model.pkl')  # Update with your model file name
data = pd.read_excel('test_dataset.xlsx')  # Update with your Excel file name

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    if request.method == 'POST':
        # Get input values from the form
        customer_id = int(request.form['customer_id'])
        
        # Fetch data for the given customer ID from the dataset
        customer_data = data[data['CustomerID'] == customer_id].iloc[0]

        # Convert the fetched data to a JSON response
        response = {
            'customer_id': customer_id,
            'Tenure': int(customer_data['Tenure']),
            'CityTier': int(customer_data['CityTier']),
            'WarehouseToHome': int(customer_data['WarehouseToHome']),
            'PreferredPaymentMode': int(customer_data['PreferredPaymentMode']),
            'Gender': int(customer_data['Gender']),
            'NumberOfDeviceRegistered': int(customer_data['NumberOfDeviceRegistered']),
            'PreferredOrderCat': int(customer_data['PreferredOrderCat']),
            'SatisfactionScore': int(customer_data['SatisfactionScore']),
            'MaritalStatus': int(customer_data['MaritalStatus']),
            'NumberOfAddress': int(customer_data['NumberOfAddress']),
            'Complain': int(customer_data['Complain']),
            'OrderCount': int(customer_data['OrderCount']),
            'DaySinceLastOrder': int(customer_data['DaySinceLastOrder']),
            'CashbackAmount': int(customer_data['CashbackAmount'])
        }

        return jsonify(response)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the JSON data
        data = request.get_json()

        # Extract input features
        customer_id = data['customer_id']
        tenure = data['Tenure']
        city_tier = data['CityTier']
        warehouse_to_home = data['WarehouseToHome']
        preferred_payment_mode = data['PreferredPaymentMode']
        gender = data['Gender']
        num_devices_registered = data['NumberOfDeviceRegistered']
        preferred_order_cat = data['PreferredOrderCat']
        satisfaction_score = data['SatisfactionScore']
        marital_status = data['MaritalStatus']
        num_addresses = data['NumberOfAddress']
        complain = data['Complain']
        order_count = data['OrderCount']
        day_since_last_order = data['DaySinceLastOrder']
        cashback_amount = data['CashbackAmount']

        # Perform prediction using the model
        prediction = model.predict([[tenure, city_tier, warehouse_to_home, preferred_payment_mode, gender, num_devices_registered, 
                                     preferred_order_cat, satisfaction_score, marital_status, num_addresses, complain, order_count, day_since_last_order, cashback_amount]])

        # Map the prediction result to a human-readable format
        prediction_result = "Churn" if prediction[0] == 1 else "Not Churn"

        # Save the prediction result with feature names and values to a text file
        with open('result.txt', 'a') as file:
           file.write(f'CustomerID: {customer_id}, Tenure: {tenure}, CityTier: {city_tier}, WarehouseToHome: {warehouse_to_home}, '
           f'PreferredPaymentMode: {preferred_payment_mode}, Gender: {gender}, NumberOfDeviceRegistered: {num_devices_registered}, '
           f'PreferredOrderCat: {preferred_order_cat}, SatisfactionScore: {satisfaction_score}, MaritalStatus: {marital_status}, '
           f'NumberOfAddress: {num_addresses}, Complain: {complain}, OrderCount: {order_count}, DaySinceLastOrder: {day_since_last_order}, '
           f'CashbackAmount: {cashback_amount}, Prediction: {prediction_result}\n')


        # Return the prediction result
        return jsonify(prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
