from flask import Flask, request
from flask import jsonify, abort

from fraction_classes import FractionParser
from test_runner import TestRunner

CONTENT_TYPE = {'Content-Type': 'text/plain'}

app = Flask(__name__)


def dict_to_textplain(d: dict):
    return '\n'.join([k + '\t' + v for k, v in d.items()])


@app.before_request
def check_if_json():
    if request.method == "POST" and request.headers["content-type"] not in ["application/json", "text/plain"]:
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

    return dict_to_textplain(result), 200, CONTENT_TYPE


@app.route("/calc", methods=["POST"])
def calc():
    if request.headers["content-type"] == "application/json":
        equation = request.json["equation"]
    else:
        try:
            equation = request.get_data().decode("utf-8").split("\t")[1]
        except Exception as e:
            return dict_to_textplain({"error": "Not valid expression"}), 400, CONTENT_TYPE

    parser = FractionParser()

    try:
        result = parser.process(equation)
    except ValueError as e:
        return dict_to_textplain({"equation": equation, "error": str(e)}), 400, CONTENT_TYPE

    return dict_to_textplain({
        "equation": equation,
        "result": result
    }), 200, CONTENT_TYPE


if __name__ == "__main__":
    app.run(host="0.0.0.0")
