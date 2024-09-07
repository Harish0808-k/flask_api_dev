from models import db


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
