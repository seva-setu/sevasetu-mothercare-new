import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    print 'Running'
    logger.info("Booting up the main server")

main()
