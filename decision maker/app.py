from flask import Flask, jsonify, render_template, request

from decisions import get_decision, get_motivation, get_random_insult


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/decide")
def decide():
    question = request.args.get("question", "").strip()

    if not question:
        return jsonify({"error": "Please enter a question before asking for a decision."}), 400

    result = get_decision(question)
    return jsonify(result), 200


@app.get("/random-insult")
def random_insult():
    return jsonify({"message": get_random_insult()}), 200


@app.get("/motivation")
def motivation():
    return jsonify({"message": get_motivation()}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
