import logging
import os
from datetime import datetime

# Create a log file name based on the current date
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"

# Define the path for the logs directory
logs_path = os.path.join(os.getcwd(), "logs")

# Ensure the logs directory exists
os.makedirs(logs_path, exist_ok=True)

# Construct the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] - %(lineno)d - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# if __name__ == "__main__":
#     logging.debug("This is a debug message")
#     logging.info("This is an info message")
#     logging.warning("This is a warning message")
#     logging.error("This is an error message")
#     logging.critical("This is a critical message")