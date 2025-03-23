import logging
from flask import Blueprint, jsonify

LOGGER = logging.getLogger(__name__)
health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"success": True, "message": "api is online"})