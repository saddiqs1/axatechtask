import logging
import traceback

from flask import Blueprint, jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound

LOGGER = logging.getLogger(__name__)
error_bp = Blueprint("errors", __name__)


@error_bp.app_errorhandler(NotFound)
def handle_not_found(error):
    LOGGER.warning(traceback.format_exc())
    return jsonify({"success": False, "message": "This resource isn't available", "error": str(error)}), 404


@error_bp.app_errorhandler(ValidationError)
def handle_invalid_data(error):
    LOGGER.warning(traceback.format_exc())
    return jsonify({"success": False, "message": "Incorrect schema for data request", "error": str(error)}), 400


@error_bp.app_errorhandler(Exception)
def handle_generic_exception(error):
    LOGGER.error(traceback.format_exc())
    return (
        jsonify({"success": False, "message": "Unknown error occurred", "error": str(error)}),
        500,
    )