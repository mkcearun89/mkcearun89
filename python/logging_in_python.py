import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This is debug')
logging.info('This is bug')
logging.warning('This is warning')
logging.error('This is error')
logging.critical('This is critical')
