from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import pickle
import pandas as pd
from explain import explain_prediction
from log_crypto import log_action
import shap
import os

app = Flask(__name__)

# ✅ Enable CORS for /api/* routes from localhost:8000
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8000"}})

# Load model and encoder
with open("backend/loan_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("backend/label_encoder.pkl", "rb") as f:
    le = pickle.load(f)


@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.json

    input_df = pd.DataFrame([data])
    for col in [
        "Gender",
        "Married",
        "Dependents",
        "Education",
        "Self_Employed",
        "Property_Area",
    ]:
        input_df[col] = le.transform(input_df[col])

    prediction = model.predict(input_df)[0]
    pred_label = le.inverse_transform([prediction])[0]

    # Explain and log
    shap_values, explainer = explain_prediction(input_df, return_explainer=True)

    # Save SHAP force plot
    os.makedirs("shap_visuals", exist_ok=True)
    shap.save_html(
        "shap_visuals/force_plot.html",
        shap.force_plot(
            base_value=explainer.expected_value,
            shap_values=shap_values[0],
            features=input_df.iloc[0],
            feature_names=input_df.columns.tolist(),
        ),
    )

    log_action("PredictionMade", str(data))

    return jsonify({"prediction": pred_label})


if __name__ == "__main__":
    app.run(debug=True)
