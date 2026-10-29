import os
import logging
from datetime import datetime

# Base directory of the project (two levels up from this file: dependencies/ -> src/ -> project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# SingletonLogger class is a singleton implementation of a logger 
# that provides a centralized logging mechanism for the application.
# This way multiple instances of the logger are not created, and all log messages are 
# handled by a single logger instance.
# We can have multiple routers and modules and they can create multiple instances of the logger, 
# but all log messages will be handled by the same logger instance.
class SingletonLogger:
    
    _instances = {}

    # The __new__ method is overridden to control the instantiation of the SingletonLogger class.
    # It checks if an instance with the given name already exists in the _instances dictionary.
    # If it does not exist, it creates a new instance and initializes the logger with the specified name, 
    # log directory, and log level.
    # If an instance already exists, it returns the existing instance, ensuring that only one 
    # instance of the logger is created for each unique name.
    # Even multiple workers can create multiple instances of the logger, 
    # but all log messages will be handled by the same logger instance.
    def __new__(cls, name , log_dir , log_level=logging.INFO):
        if cls._instances.get(name) is None:
            cls._instances[name] = super(SingletonLogger, cls).__new__(cls)
            cls._instances[name].initialize_logger(name, log_dir, log_level)
        return cls._instances[name]

    def initialize_logger(self, name, log_dir, log_level):
        """
        Initialize the logger with the specified name, log directory, and log level.

        Args:
            name (str): The name of the logger.
            log_dir (str): The directory where log files will be stored.
            log_level (int): The logging level (e.g., logging.INFO, logging.DEBUG).
        """
        self.logger = logging.getLogger(name)
        if not self.logger.hasHandlers():
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            handler = logging.FileHandler(os.path.join(log_dir, f"{name}_{timestamp}.log"),mode='a')
            handler.setFormatter(formatter)
            self.logger.setLevel(log_level)
            self.logger.addHandler(handler)

    def get_logger(self):
        """
        Get the logger instance.

        Returns:
            logging.Logger: The logger instance.
        """
        return self.logger  


#Create a logger instances for the routers and modules.
user_data_logger = SingletonLogger("user_data_router", os.path.join(BASE_DIR, "logs", "user_data_logs")).get_logger()
