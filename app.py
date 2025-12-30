from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Load trained model and feature columns
model = joblib.load("rf_house_price_model.joblib")
model_columns = joblib.load("rf_model_columns.joblib")

# Load dataset to get all unique categorical values
df = pd.read_csv("mumbai-house-price-data-cleaned.csv")

# Extract unique values for dropdowns
categorical_options = {
    'locality': sorted(df['locality'].dropna().unique()),
    'property_type': sorted(df['property_type'].dropna().unique()),
    'furnished': sorted(df['furnished'].dropna().unique())
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        data = {}
        for col in model_columns:
            if col in request.form:
                val = request.form[col]
                try:
                    val = float(val)
                except:
                    val = val
                data[col] = val

        df_input = pd.DataFrame([data])

        for col in model_columns:
            if col not in df_input.columns:
                df_input[col] = 0

        df_input = df_input[model_columns]

        predicted_price = model.predict(df_input)[0]

        result = {"predicted_price": round(predicted_price, 2)}

    return render_template("index.html", result=result, options=categorical_options)

if __name__ == "__main__":
    app.run(debug=True)