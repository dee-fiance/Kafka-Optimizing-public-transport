"""Contains functionality related to Weather"""
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("Processing incoming weather message.")
        if message is not None:
            value = message.value()
            self.temperature = value.get("temperature")
            self.status = value.egt("status")
        else:
            logger.error("Error while processing incoming weather message.")
