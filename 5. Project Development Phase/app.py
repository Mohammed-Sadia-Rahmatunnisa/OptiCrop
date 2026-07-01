from flask import Flask, render_template, request
import pickle
import numpy as np
from crop_data import crop_info

app = Flask(__name__)

# ----------------------------
# Load Trained Model
# ----------------------------
with open("model/crop_model.pkl", "rb") as file:
    model = pickle.load(file)


# ----------------------------
# Home Page
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------
# About Page
# ----------------------------
@app.route("/about")
def about():
    return render_template("about.html")


# ----------------------------
# Prediction
# ----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    try:

        nitrogen = float(request.form["nitrogen"])
        phosphorus = float(request.form["phosphorus"])
        potassium = float(request.form["potassium"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        data = np.array([[
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        ]])

        prediction = model.predict(data)[0].lower()

        image = f"images/crops/{prediction}.jpg"

        confidence = None

        if hasattr(model, "predict_proba"):

            probability = model.predict_proba(data)

            confidence = round(
                np.max(probability) * 100,
                2
            )

        crop = crop_info.get(
            prediction,
            {
                "season": "Not Available",
                "soil": "Not Available",
                "temperature": "Not Available",
                "humidity": "Not Available",
                "rainfall": "Not Available",
                "water": "Not Available",
                "harvest": "Not Available",
                "fertilizer": "Not Available",
                "tips": "Information not available.",
                "image": "images/crops/default.jpg"
            }
        )

        crop["image"] = image

        return render_template(
            "index.html",
            prediction=prediction.title(),
            confidence=confidence,
            crop=crop,
            values=request.form
        )

        

    except Exception as e:

        return render_template(

            "index.html",

            error=str(e),

            values=request.form

        )


# ----------------------------
# Run Application
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)