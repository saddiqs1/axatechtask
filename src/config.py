import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    LOGGING = {
        "version": 1,
        "filters": {},
        "formatters": {
            "standard": {"format": "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"},
            "compact": {"format": "%(asctime)s %(levelname)s\t%(message)s"},
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "compact",
                "stream": "ext://sys.stdout",
                "filters": [],
            }
        },
        "loggers": {
            "": {"handlers": ["console"], "level": "DEBUG"},
            "flask": {"level": "WARNING"},
            "sqlalchemy": {"level": "WARNING"},
            "werkzeug": {"level": "WARNING"},
        },
        "disable_existing_loggers": False,
    }