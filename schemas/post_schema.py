from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validates
)
from main import db
from user_schema import UserSchemaOut
from models.user_model import User


class PostSchemaIn(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    image = fields.String(required=True)
    author = fields.String(required=True)

    @validates('title')
    def validate_title(self, value):
        if len(value) < 10 or len(value) > 50:
            raise ValidationError(
                "Title can be between 10 to 50 characters only."
            )

    @validates('description')
    def validate_description(self, value):
        if len(value) > 500 or len(value) < 3:
            raise ValidationError(
                (
                    "Description should be not more than 500 characters and "
                    "less than 3 characters."
                )
            )

    @validates('image')
    def validate_image_extension(self, value):
        if not value.lower().endswith(('.jpg', '.jpeg', '.png')):
            raise ValidationError(
                "Image must have .jpg, .jpeg or .png extension"
            )

    @validates('author')
    def validate_author(self, value):
        user_obj = db.session.query(User).filter_by(name=value).first()
        if not user_obj:
            raise ValidationError(
                f"Author doesn't exists with the username {value}"
            )
        else:
            self.context['user_id'] = user_obj.id


class PostSchemaOut(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    image = fields.String()
    author = fields.Nested(UserSchemaOut)
    created_on = fields.DateTime()
    updated_on = fields.DateTime()
