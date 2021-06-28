from utilities.logging.sinks import add_terminal_sink, add_custom_sink, add_file_sink
from loguru import logger


def initialize_logging():
    """
    Initializes logging handlers and sinks. New sinks and handlers
    should be registered in this function.
    """

    # All logs emitted by 1) the intercepter and 2) all loguru.logger.* method calls
    # will be sent to a loguru sink. Sinks are simply destinations for logging data.
    # By default, we add two sinks; one for sending logs to the console and to a file.
    # To send logs to a database, e.g. an Elasticsearch instance, simply add a custom
    # sink to send the data there.
    # See https://loguru.readthedocs.io/en/stable/api/logger.html for details.
    add_file_sink(logger)
    add_terminal_sink(logger)

    # Arbitrary sinks to process raw log records (for sending to log databases for example)
    # can be configured as such:
    add_custom_sink(logger, lambda record: print(
        f'Received raw log record: {record}'
    ))
