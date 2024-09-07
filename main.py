import os
from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

# if True, it will track modification of model objects(records)
# it will be overloaded. sqlalchemy says put it to False only.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize db and migrations by creating instances
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(125), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_on = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    # establishing relationship with Post Model
    post = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"{self.id} - {self.name}"


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)

    # store image path in the db and image can be stored in S3 bucket
    # or folder on server but now a days it is stored in cloud platforms
    image = db.Column(db.String(255), nullable=False)

    # creating a foreign key relationship
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class LikeAndComment(db.Model):
    __tablename__ = 'likesandcomments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    is_like = db.Column(db.Boolean, default=False, nullable=False)
    comment = db.Column(db.String(255), nullable=False)

    created_on = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_on = db.Column(db.DateTime,
                           default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp()
                           )

    # Relationships to User and Post models for easy access like
    # user.likes_and_comments and post.likes_and_comments
    user = db.relationship('User', backref='likes_and_comments')
    post = db.relationship('Post', backref='likes_and_comments')


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
