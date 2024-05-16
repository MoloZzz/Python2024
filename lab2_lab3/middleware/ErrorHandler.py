# ErrorHandler.py
from flask import jsonify

def handle_exception(app):
    @app.errorhandler(Exception)
    def handle_all_exceptions(e):
        response = {
            "error": str(e),
            "type": type(e).__name__
        }
        return jsonify(response), 500

    @app.errorhandler(400)
    def handle_bad_request(e):
        response = {
            "error": "Bad request",
            "message": str(e)
        }
        return jsonify(response), 400

    @app.errorhandler(404)
    def not_found(e):
        response = {
            "error": "Resource not found",
            "message": str(e)
        }
        return jsonify(response), 404
