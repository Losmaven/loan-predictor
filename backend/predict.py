# backend/predict.py

from flask import Flask, request, jsonify
import pickle
import pandas as pd
from explain import explain_prediction
from log_crypto import log_action

app = Flask(__name__)

# Load model and encoder
with open('backend/loan_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('backend/label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json

    input_df = pd.DataFrame([data])
    for col in ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']:
        input_df[col] = le.transform(input_df[col])

    prediction = model.predict(input_df)[0]
    pred_label = le.inverse_transform([prediction])[0]

    # Explain and log
    shap_info = explain_prediction(input_df)
    log_action('PredictionMade', str(data))

    return jsonify({'prediction': pred_label, 'shap_summary': shap_info})

if __name__ == '__main__':
    app.run(debug=True)
