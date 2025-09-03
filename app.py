from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("credit_model.joblib")
scaler = joblib.load("scaler.joblib")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            data = request.get_json()
            features = [float(x) for x in data.values()]
        else:
            features = [float(x) for x in request.form.values()]
        

        final_features = np.array(features).reshape(1, -1)
        final_features = scaler.transform(final_features)
        prediction = model.predict(final_features)[0]
        result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"

        if request.is_json:
            return jsonify({"prediction": int(prediction), "result": result})
        else:
            return render_template("result.html", prediction=result)

    except Exception as e:
        if request.is_json:
            return jsonify({"error": str(e)})
        else:
            return render_template("result.html", prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
