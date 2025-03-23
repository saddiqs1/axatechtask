import logging
from flask import Blueprint, jsonify
from decorators import log_endpoint

LOGGER = logging.getLogger(__name__)
health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
@log_endpoint
def health_check():
    return jsonify({"success": True, "message": "api is online"}), 200