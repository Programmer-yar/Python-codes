import logging

#By default only 'WARNING', 'ERROR', 'CRITICAL' are displayed

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# output format: LEVEL:NAME:MESSAGE

#this also display DEBUG level messages, write at the start of document
logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')