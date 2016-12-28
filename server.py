import logging

from mothercare import app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():

    print 'Running'
    logger.info("Booting up the main server")

    runnable = app.endpoints()
    runnable.run(host='0.0.0.0', port=80, server='waitress', loglevel='warning')

main()
