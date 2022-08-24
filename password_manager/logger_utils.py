import logging
import os

class LogFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    reset = "\x1b[0m"
    fmt = "%(levelname)s - %(message)s"

    FORMATS = {
        logging.INFO: grey + fmt + reset,
        logging.WARNING: yellow + fmt + reset,
        logging.ERROR: red + fmt + reset,
    }

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        if log_fmt:
            self._fmt = log_fmt
            self._style._fmt = log_fmt
        return super().format(record)

def get_logger(
    name: str = "PASSWORD_RESET",
    level: int = None,
) -> logging.Logger:
    """Logger initializer with custom formatter.
    Args:
        name (str): Name of logger to use.
        level (int, optional): level for logger. Defaults to None.
    Returns:
        [type]: [description]
    """
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(LogFormatter())
    logger.addHandler(handler)
    logger.setLevel(level=level or logging.INFO)
    return logger
