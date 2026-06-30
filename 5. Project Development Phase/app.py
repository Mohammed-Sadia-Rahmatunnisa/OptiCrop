from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
print("APP.PY LOADED SUCCESSFULLY")
# Load the trained model
model = pickle.load(open("model/crop_recommendation_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    nitrogen = float(request.form["nitrogen"])
    phosphorus = float(request.form["phosphorus"])
    potassium = float(request.form["potassium"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    print("PREDICT ROUTE CALLED")

    data = np.array([[nitrogen,
                      phosphorus,
                      potassium,
                      temperature,
                      humidity,
                      ph,
                      rainfall]])

    prediction = model.predict(data)

    return render_template(
        "index.html",
        prediction_text=f"Recommended Crop: {prediction[0]}"
    )

print("Registered Routes:")
print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)