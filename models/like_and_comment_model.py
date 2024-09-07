from models import db


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
