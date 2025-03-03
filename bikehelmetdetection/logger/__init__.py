import logging  # Importing the logging module for logging error messages and events
import os  # Importing the os module for interacting with the file system
from datetime import datetime  # Importing datetime module to timestamp log files
from from_root import from_root  # Importing from_root to get the root directory of the project

# Generating a log file name using the current date and time in 'MM_DD_YYYY_HH_MM_SS' format
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Defining the path where logs will be stored, inside the 'log' directory in the root folder
log_path = os.path.join(from_root(), 'log', LOG_FILE)

# Creating the log directory if it does not exist
os.makedirs(log_path, exist_ok=True)

# Constructing the full path for the log file
lOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configuring the logging settings
logging.basicConfig(
    filename=lOG_FILE_PATH,  # Setting the log file path
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",  # Defining the log format
    level=logging.INFO  # Setting the logging level to INFO to capture informational messages and above
)
