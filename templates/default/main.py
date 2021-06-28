
# --- Welcome to your Emily project! --- #

from loguru import logger 
from utilities.logging.config import initialize_logging


initialize_logging()

if __name__ == '__main__':
    logger.info("Hello World!")
