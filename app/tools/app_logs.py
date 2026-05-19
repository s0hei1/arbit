from __future__ import annotations

import logging
import logging.config
import os
from contextvars import ContextVar


trace_id_var: ContextVar[str | None] = ContextVar("trace_id", default="1")
user_id_var: ContextVar[str | None] = ContextVar("user_id", default="s0hei1")


class ContextFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.trace_id = trace_id_var.get()
        record.user_id = user_id_var.get()
        return True


def setup_logging(
    *,
    env: str | None = "development",
    log_dir: str = "logs",
    default_level: int | None = None,
) -> None:
    env = (env or os.getenv("APP_ENV", "production")).lower()

    if default_level is None:
        default_level = logging.DEBUG if env in {"dev", "development", "local"} else logging.INFO

    os.makedirs(log_dir, exist_ok=True)

    # Human-readable formats
    standard_fmt = (
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # dictConfig allows defining the whole system in one place
    config = {
        "version": 1,
        "disable_existing_loggers": False,

        "filters": {
            "context": {"()": ContextFilter},
        },

        "formatters": {
            "standard": {
                "format": standard_fmt,
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": default_level,  # INFO in prod, DEBUG in dev
                "formatter": "standard",
                "filters": ["context"],
                "stream": "ext://sys.stdout",
            },

            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": logging.DEBUG,
                "formatter": "standard",
                "filters": ["context"],
                "filename": os.path.join(log_dir, "app.log"),
                "maxBytes": 10 * 1024 * 1024,  # 10MB
                "backupCount": 5,
                "encoding": "utf-8",
            },
        },

        "root": {
            "level": default_level,
            "handlers": ["console", "file"],
        },

        # "loggers": {
        #     "uvicorn": {"level": "WARNING", "propagate": True},
        #     "werkzeug": {"level": "WARNING", "propagate": True},
        #     "sqlalchemy.engine": {"level": "WARNING", "propagate": True},
        # },
    }

    logging.config.dictConfig(config)