import functools
import logging
import time
from flask import request

LOGGER = logging.getLogger(__name__)

def log_endpoint(func):
    """
    Decorator to log the time elapsed by the decorated method.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        response = func(*args, **kwargs)
        elapsed = time.time() - start

        status_code = response[1]

        LOGGER.info(
            f"{request.method} {request.path}: {build_key(func)} took {elapsed:.4f} seconds, status code: {status_code}"
        )
        return response
    return wrapper

def build_key(func):
    return f"{func.__module__}:{func.__name__}"
