from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route("/")
def health_check():
    # make_response adds flexibilty for to add headers, modify response
    # modify status code, gives more control over how responses are returned.

    response = make_response(
        jsonify(
            {
                "message": "Service is up and running."
            }
        ), 200
    )
    # provides metadata
    response.headers['API-version'] = "0.0.1"
    response.headers['Served-By'] = "My Flask app"
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
