# backend/explain.py

import shap
import matplotlib.pyplot as plt

# Load your trained model
import pickle
with open('backend/loan_model.pkl', 'rb') as f:
    model = pickle.load(f)

def explain_prediction(input_df, return_explainer=False):
    explainer = shap.Explainer(model)
    shap_values = explainer(input_df)

    # Optionally generate a summary plot (not required for force plot)
    plt.clf()
    shap.summary_plot(shap_values, input_df, show=False)

    if return_explainer:
        return shap_values, explainer

    return "SHAP explanation complete"
