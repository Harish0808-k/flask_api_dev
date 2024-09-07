import os
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from models import db

load_dotenv()

app = Flask(__name__)


# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

# if True, it will track modification of model objects(records)
# it will be overloaded. sqlalchemy says put it to False only.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize db and migrations by creating instances
db.init_app(app)
migrate = Migrate(app, db)


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
    response.headers["API-version"] = "0.0.1"
    response.headers["Served-By"] = "My Flask app"
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
