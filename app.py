from flask import Flask, render_template, request
import pickle
from feature_extraction import extract_features

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        prediction = model.predict([features])

        if prediction[0] == 1:
            result = "⚠️ Phishing Website"
        else:
            result = "✅ Legitimate Website"

    return f"""
    <html>
    <head>
        <title>Phishing Detection</title>
    </head>
    <body style="text-align:center;font-family:Arial;margin-top:100px;">
        <h1>Phishing Website Detection System</h1>
        <form method="post">
            <input type="text" name="url" placeholder="Enter URL" size="50" required>
            <br><br>
            <button type="submit">Check</button>
        </form>
        <h2>{result if result else ""}</h2>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
