from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)
data = pd.read_csv("new_data.csv")
pipe = pickle.load(open("RegressionModel.pkl", "rb"))


@app.route("/")
def index():
    bedrooms = sorted(data["Bedrooms"].unique())
    bathrooms = sorted(data["Bathrooms"].unique())
    neighborhoods = ["Rural", "Suburb", "Urban"]
    years_built = sorted(data["YearBuilt"].unique())

    return render_template(
        "index.html",
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        neighborhoods=neighborhoods,
        years_built=years_built,
    )


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Log the form data
        bedrooms = request.form.get("Bedrooms")
        bathrooms = request.form.get("Bathrooms")
        square_feet = request.form.get("SquareFeet")
        neighborhood = request.form.get("Neighborhood")
        year_built = request.form.get("YearBuilt")

        print(
            f"Received form data: Bedrooms={bedrooms}, Bathrooms={bathrooms}, SquareFeet={square_feet}, Neighborhood={neighborhood}, YearBuilt={year_built}"
        )

        # Convert form data to the appropriate types
        bedrooms = int(bedrooms)
        bathrooms = float(bathrooms)
        square_feet = float(square_feet)
        neighborhood = str(neighborhood)
        year_built = int(year_built)

        # Create a DataFrame with the input data
        input_data = pd.DataFrame(
            [[square_feet, bedrooms, bathrooms, year_built]],
            columns=["SquareFeet", "Bedrooms", "Bathrooms", "YearBuilt"],
        )

        # One-hot encode the 'Neighborhood' column
        neighborhoods = ["Rural", "Suburb", "Urban"]
        for n in neighborhoods:
            input_data[n] = 1 if neighborhood == n else 0

        print("Input Data DataFrame after encoding:")
        print(input_data)

        # Predict the price using the loaded pipeline
        prediction = pipe.predict(input_data)[0]
        print(f"Prediction: {prediction}")

        return jsonify({"price": prediction})

    except Exception as e:

        print(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
