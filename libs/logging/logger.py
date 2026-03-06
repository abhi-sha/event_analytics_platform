import logging
import structlog


def configure_logging():
    logging.basicConfig(
        format="%(message)s",
        level=logging.INFO
    )


    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
    )

def get_logger():
    return structlog.get_logger()