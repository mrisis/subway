import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('metro.log')

c_format = logging.Formatter("%(asctime)s -\t %(name)s - %(levelname)s\t - %(message)s")

console_handler.setFormatter(c_format)
file_handler.setFormatter(c_format)

console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
