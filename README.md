# LoanApproval-XAI-Crypto 🧠🔒

A full-stack project to predict loan approval using Machine Learning, Explainable AI (SHAP), and cryptographic audit logging.

## 🚀 Features
- Random Forest ML model for binary classification
- SHAP explanations with summary & force plots
- Cryptographic audit logging (SHA-256)
- Single-page frontend for visual interaction

## 📁 Folder Structure

LoanApproval-XAI-Crypto/
│
├── backend/
│   ├── loan_dataset.csv        ✅ Final dataset (100 samples)
│   ├── model.py                🧠 Train & save ML model
│   ├── predict.py              🔮 Predict endpoint via Flask
│   ├── explain.py              📊 SHAP explainability
│   ├── log_crypto.py           🔐 Cryptographic secure logger
│
├── frontend/
│   ├── index.html              🌐 Stylish single-page UI
│   ├── styles.css              🎨 CSS styling
│   └── script.js               ⚙️ JS to interact with backend API
│
├── shap_visuals/
│   ├── force_plot.html         📈 Generated during runtime
│   └── summary_plot.png        📊 Generated during runtime
│
├── logs/
│   └── audit_log.csv           📝 Cryptographically hashed log
│
├── requirements.txt            📦 Python dependencies
└── README.md                   📘 Full setup + run instructions

## How it works

# Step 1: Go to your project directory
cd LoanApproval-XAI-Crypto (directory name you choose)

# Step 2: Create a virtual environment (optional but recommended)
python -m venv env
source env/bin/activate     # On Windows, use:
                            # env\Scripts\activate

# Step 3: Install all dependencies
pip install -r requirements.txt

# Step 4: Train the machine learning model (this saves model & encoder)
python backend/model.py

# Step 5: Start the Flask API server
python backend/predict.py



## if wanted to run again after closing

env\Scripts\activate

## to restart 
python backend/predict.py

# setup frontend 
cd frontend
python -m http.server 8000

http://localhost:8000