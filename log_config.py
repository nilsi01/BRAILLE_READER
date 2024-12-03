import logging

# Set up logging configuration
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler("log.log", mode='w')  # Log to a file
    ]
)

