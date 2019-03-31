from flask import Flask, jsonify, request, abort

from fraction_classes import FractionParser
from test_runner import TestRunner

app = Flask(__name__)


@app.before_request
def check_if_json():
    if request.method == "POST" and request.headers["content-type"] != "application/json":
        abort(400)


@app.route("/", methods=["GET"])
def index():
    return """<h1>Small fraction calculator app.</h1><br> 
/healthcheck (GET) \t-\t info on if system is OK<br>
/calc (POST - {"equation": "$equation"} \t-\t returns the result of calculation in the format
 {\"equation\": "$equation", "result": "$result"}<br> 
"""


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
        return jsonify({"equation": equation, "error": str(e)}), 400

    return jsonify({
        "equation": equation,
        "result": result
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
