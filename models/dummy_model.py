from models import db


class Dummy(db.Model):
    __tablename__ = "dummies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))

    def __repr__(self) -> str:
        return self.name
