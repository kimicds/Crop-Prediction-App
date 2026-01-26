from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import joblib

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Load trained model and scaler
model = joblib.load("final_model.joblib")
scaler = joblib.load("scaler.joblib")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            # Numeric features
            features = [
                'Soil_pH', 'Potassium_K', 'Phosphorus_P', 'Nitrogen_N',
                'Zinc_Zn', 'Sulphur_S', 'Rainfall', 'Temperature', 'Humidity'
            ]

            input_data = {col: float(request.form[col]) for col in features}

            # Soil color (manual dummy encoding)
            soil_color = request.form["Soil_Color"]
            for color in ['black', 'brown', 'reddish brown']:
                input_data[f"Soil_Color_{color}"] = 1 if soil_color == color else 0

            df = pd.DataFrame([input_data])

            # ✅ Scale NUMERIC columns exactly how model was trained
            #for col in features:
                #df[col] = scaler.transform(df[[col]])

            # Prediction
            pred = model.predict(df)[0]
            crop = "Maize" if pred == 0 else "Rice"

            # Save for manual retraining
            df["Crop_Type_Predicted"] = pred
            df.to_csv("collected_data.csv", mode="a", header=False, index=False)

            # ✅ Redirect to result page
            return redirect(url_for("result", crop=crop))

        except Exception as e:
            flash(f"Prediction failed: {str(e)}")
            return redirect(url_for("predict"))

    return render_template("predict.html")


@app.route("/result")
def result():
    crop = request.args.get("crop")
    return render_template("result.html", crop=crop)


if __name__ == "__main__":
    app.run(debug=True)