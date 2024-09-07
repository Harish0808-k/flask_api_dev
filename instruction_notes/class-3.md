#### Serialization and Deserialization

- `Serialization` is a process of converting Python objects(Models) to JSON format.

- `Deserialization` is a process of converting JSON format to Python Objects.

#### How to perform Serialization and Deserialization?
#### Manual Way:
#### Serialization:
```python
from flask import jsonify

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    email = db.Column(db.String(125), nullable=False, unique=True)
    created_on = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_on = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_on': self.created_on.isoformat(),
            'updated_on': self.updated_on.isoformat()
        }

@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.serialize()), 200

```
In this example:

- The `serialize()` method in the `User` model returns a dictionary of the user's data in a JSON-friendly format.

- In the route `/users/<int:user_id>`, the `serialize()` method is used to convert the model instance into JSON before returning it.

#### Deserialization:
```python
from flask import request

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Invalid input"}), 400

    # Deserializing data to Python objects
    new_user = User(
        name=data['name'],
        email=data['email']
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.serialize()), 201
```
In this example:

- The `request.get_json()` method is used to deserialize the incoming JSON into a Python dictionary.

- We then use this data to create a new `User` object and save it to the database.

#### Use `marshmallow` for Automatic Serialization/Deserialization
`marshmallow` is a library that automates serialization and deserialization for Flask. It helps manage validation and transformation between objects and data.

```bash
pip install marshmallow
```
