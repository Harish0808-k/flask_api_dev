from flask import jsonify, make_response


def success_response(message, data, status_code):
    return make_response(
        jsonify(
            {
                "message": message,
                "data": data,
                "success": True
            }
        ), status_code
    )


def error_response(error_message, error_detail, status_code):
    return make_response(
        jsonify(
            {
                "error_message": error_message,
                "error_detail": error_detail,
                "success": False
            }
        ), status_code
    )
