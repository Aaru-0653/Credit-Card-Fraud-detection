💳 Credit Card Fraud Detection

Detect fraudulent transactions using Machine Learning and a Flask web app.
This project trains a model on real credit card transaction data and provides a simple web interface to test predictions.

CREDIT-CARD-FRAUD-DETECTION/
│
├── Dataset/
│   └── creditcard_2023.csv        # Dataset used for training
│
├── static/                        # CSS for styling
│   ├── style.css
│   └── result.css
│
├── templates/                     # HTML templates
│   ├── index.html
│   └── result.html
│
├── app.py                         # Flask web app
├── model_building.py              # Training script
├── cancer_model.joblib            # Trained model
├── scaler.joblib                  # Scaler for normalization
├── requirements.txt               # Project dependencies
├── runtime.txt                    # Python version for deployment
└── README.md                      # Project documentation


📊 Dataset

Source: Kaggle - Credit Card Fraud Detection Dataset
## Dataset
The dataset used for training this model can be found here:  
[Credit Card Fraud Detection Dataset on Kaggle] https://www.kaggle.com/datasets/nelgiriyewithana/credit-card-fraud-detection-dataset-2023?utm_source=chatgpt.com

Features: 30 numerical features (V1 → V28, Amount)
Target: Class
0 → Legitimate Transaction
1 → Fraudulent Transaction

⚙️ How It Works

Preprocess dataset using pandas and scikit-learn.
Train a classification model.
Save model + scaler using joblib.
Deploy Flask app where users can input transaction values and get predictions.



🖥️ Setup & Installation

Clone the repository:
git clone https://github.com/Aaru-0653/Credit-Card-Fraud-detection.git
cd Credit-Card-Fraud-Detection

Create & activate a virtual environment:
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows

Install dependencies:
pip install -r requirements.txt

Run the Flask app:
python app.py

Open in browser:
http://127.0.0.1:5000



"C:\Users\aarup\Pictures\Screenshots\Screenshot 2025-09-03 124440.png"
🔹 Input Form
(User enters transaction details)


"C:\Users\aarup\Pictures\Screenshots\Screenshot 2025-09-03 124501.png"
🔹 Prediction Result
✅ Legitimate Transaction
🚨 Fraudulent Transaction


🛠️ Tech Stack

Python
Flask
scikit-learn
pandas, numpy
joblib (model persistence)
HTML, CSS (Frontend)


🙌 Acknowledgments

Dataset by Kaggle
Inspired by real-world fraud detection use cases
