from flask import Flask, request, jsonify
from analyze import analyze_website

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    url = request.json["url"]
    result = analyze_website(url)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
