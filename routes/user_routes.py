from flask import Blueprint
from models import db
# from schemas.user_schema import UserSchemaOut
from utilities.custom_response import error_response, success_response
from models.user_model import User


users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
def register():
    try:
        users = db.session.query(User).all()
        print(users)
        if users:
            # user_schema_out = UserSchemaOut(many=True)
            data = users
        else:
            data = []
        return success_response(
                                message="users fetched successfully",
                                data=data,
                                status_code=200
                            )
    except Exception as ex:
        return error_response(
            error_message="Something went wrong.",
            error_detail=str(ex),
            status_code=500
        )
