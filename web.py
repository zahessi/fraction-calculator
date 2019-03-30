from flask import Flask, jsonify, request
from fraction_classes import TestRunner, FractionParser

app = Flask(__name__)


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    t = TestRunner().run()
    result = {"status": "all good"}

    if t:
        result = {"status": "error on the server side"}

    return jsonify(result)


@app.route("/calc", methods=["POST"])
def calc():
    equation = request.json["equation"]

    parser = FractionParser()

    try:
        result = parser.process(equation)
    except ValueError as e:
        return jsonify({"error": str(e)}, 400)
    else:
        return jsonify({
            "equation": equation,
            "result": result
        }, 200)


if __name__ == "__main__":
    app.run()
