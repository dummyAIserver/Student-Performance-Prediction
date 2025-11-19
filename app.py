from flask import Flask, render_template, request # type: ignore
import pickle
import numpy as np # type: ignore

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html", message="Please enter attendance, assignment, and internal marks to predict final marks.")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        attendance = float(request.form['attendance'])
        assignment = float(request.form['assignment'])
        internal = float(request.form['internal'])
    except ValueError:
        return render_template("index.html", error_message="Error: All inputs must be valid numbers.")

    if not (0 <= attendance <= 100):
        return render_template("index.html", error_message="Error: Attendance must be between 0 and 100.")
    if not (0 <= assignment <= 100):
        return render_template("index.html", error_message="Error: Assignment must be between 0 and 100.")
    if not (0 <= internal <= 100):
        return render_template("index.html", error_message="Error: Internal marks must be between 0 and 100.")

    input_data = np.array([[attendance, assignment, internal]])
    prediction = model.predict(input_data)[0]

    return render_template("index.html", prediction_result=f"Predicted Final Marks: {prediction:.2f}")

if __name__ == "__main__":
    app.run(debug=True)
    