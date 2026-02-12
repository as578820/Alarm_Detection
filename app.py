from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Flask app is running"

@app.route("/test_data", methods=["POST"])
def test_data():
    data = request.get_json()
    #print(data)
    mapping = {
        "Ambient Temperature": "Ambient Temperature( deg C)",
        "Calibration": "Calibration(days)",
        "Unwanted substance deposition": "Unwanted substance deposition(0/1)",
        "Humidity": "Humidity(%)",
        "H2S Content": "H2S Content(ppm)",
        "detected by": "detected by(% of sensors)"
    }
    test_df = pd.DataFrame([data]).rename(columns=mapping)
    #print(test_df.head())
    pipe = joblib.load("alarm_pipeline.pkl")
    pred = pipe.predict(test_df)[0]
    #res = int(pred[0])
    if pred:
        return jsonify({"result": "success",
                        "message": "Alarm detected is Dangerous",
                        "Alarm code": "101"
                        })
    else:
        return jsonify({"result": "success",
                        "message": "Alarm detected is Not Dangerous",
                        "Alarm code": "000"
                        })


# Start the server
if __name__ == "__main__":
    app.run(debug=True)
