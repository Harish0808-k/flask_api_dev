from marshmallow import (
    Schema,
    fields
)
from user_schema import UserSchemaOut
from post_schema import PostSchemaOut


class LikeAndCommentSchemaIn(Schema):
    user_id = fields.Integer(required=True)
    post_id = fields.Integer(required=True)
    is_like = fields.Boolean(required=True)
    comment = fields.String(required=True)


class LikeAndCommentSchemaOut(Schema):
    user = fields.Nested(UserSchemaOut)
    post = fields.Nested(PostSchemaOut)
    is_like = fields.Boolean()
    comment = fields.String()
    created_on = fields.DateTime()
    updated_on = fields.DateTime()
