import os
import logging
from datetime import datetime


def get_logger(file_name=None):
    ts = get_date_time() if file_name is None else file_name
    log_dir = os.path.join(os.getcwd(), 'logs', f'{ts}.log')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    info_log = logging.FileHandler(log_dir)
    info_log.setFormatter(formatter)
    info_log.setLevel(logging.INFO)
    console_log = logging.StreamHandler()
    console_log.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(info_log)
        logger.addHandler(console_log)

    return logger


def get_date_time():
    now = datetime.now()  # current date and time
    date_time = now.strftime("%m%d%Y%H%M%S")
    return date_time
