import re
from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validates,
    validates_schema
)


class UserSchemaIn(Schema):
    username = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    confirm_password = fields.String(required=True)

    @validates('username')
    def validate_name(self, value):
        if len(value) < 3 or len(value) > 15:
            return ValidationError(
                "Username must be between 3 to 15 characters."
            )

    @validates('password')
    def validate_password(self, value):
        if len(value) < 8 or len(value) > 15:
            raise ValidationError(
                "Password length should be between 8 to 15 Characters."
            )
        if not re.search(r"[a-z]", value):
            raise ValidationError(
                "Password must contain atleast one lower-case letter."
            )
        if not re.search(r"[A-Z]", value):
            raise ValidationError(
                "Password must contain atleast one upper-case letter."
            )
        if not re.search(r"[~!@#$%^&*()+_-`;:'?><.,/]", value):
            raise ValidationError(
                "Password must contain atleast one special character."
            )
        if not re.search(r"[0-9]", value):
            raise ValidationError(
                "Password must contain atleast one numeric value."
            )

    # validates_schema is performed on entire schema after
    # validating all fields
    @validates_schema
    def validate_confirm_password(self, data, **kwargs):
        if data['password'] != data['confirm_password']:
            raise ValidationError(
                "Password and Confirm Password must match.",
                field_name='confirm_password'
            )


class UserSchemaOut(Schema):
    id = fields.Integer()
    name = fields.String()
    email = fields.Email()
    created_on = fields.DateTime()
    updated_on = fields.DateTime()
