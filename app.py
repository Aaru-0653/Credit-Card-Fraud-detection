from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load("cancer_model.joblib")
scaler = joblib.load("scaler.joblib")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from form or JSON
        if request.is_json:
            # If request comes from API (JSON request)
            data = request.get_json()
            features = [float(x) for x in data.values()]
        else:
            # If request comes from HTML form
            features = [float(x) for x in request.form.values()]
        
        # Convert to numpy array & reshape
        final_features = np.array(features).reshape(1, -1)
        
        # Scale input
        final_features = scaler.transform(final_features)
        
        # Predict using model
        prediction = model.predict(final_features)[0]
        
        # Output result
        result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"

        # If request is from API -> return JSON
        if request.is_json:
            return jsonify({"prediction": int(prediction), "result": result})
        else:
            # If request is from form -> show result.html
            return render_template("result.html", prediction=result)

    except Exception as e:
        if request.is_json:
            return jsonify({"error": str(e)})
        else:
            return render_template("result.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
