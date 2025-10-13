import logging
import os
from logging.handlers import RotatingFileHandler

from utilities.constants import APP_NAME


def get_logger(name):
    os.makedirs('reports/logs', exist_ok=True) #Verifies the log folder exists
    logger = logging.getLogger(name) #Defining looger object

    # Prevent adding duplicate handlers if logger is already configured.
    if not logger.handlers:
        #Creatng Rotate File Handler to keep last 5 backup and 2MB/file, handle unicode safely using utf-8
        handler = RotatingFileHandler(f'reports/logs/{APP_NAME.replace(" ", "_").lower()}_test_log.log', maxBytes=2*1024*1024, backupCount=5, encoding='utf-8')

        #Setting up log message format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        #Console handler to print log in terminal
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        #Adding handlers to logger
        logger.addHandler(handler)
        logger.addHandler(console_handler)

        #Set the log level to info
        logger.setLevel(logging.INFO)

    #Returns the logger object
    return logger
