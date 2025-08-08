import logging
import os
from datetime import datetime

# Create timestamp
TIMESTAMP = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

# Get project root (one level up from where this file is located)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to the folder for this run's logs
run_log_dir = os.path.join(ROOT_DIR, "logs", TIMESTAMP)
os.makedirs(run_log_dir, exist_ok=True)

# Full path to the log file inside that folder
LOG_FILE_PATH = os.path.join(run_log_dir, f"{TIMESTAMP}.log")


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] line %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


