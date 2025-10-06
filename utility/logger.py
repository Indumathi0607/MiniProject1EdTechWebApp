import logging
import os


def get_logger(name):
    os.makedirs('reports/logs', exist_ok=True)
    logger = logging.getLogger(name)
    handler = logging.FileHandler('reports/logs/test_log.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger