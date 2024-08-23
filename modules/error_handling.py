import logging

def setup_logging():
    if len(logging.getLogger().handlers) == 0:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        logging.info("Logging is set up.")