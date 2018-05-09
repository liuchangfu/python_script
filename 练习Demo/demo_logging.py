import logging

logger  =logging.getLogger('mylogger')

logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('monitor.log')
fh.setLevel(logging.INFO)

ch  = logging.StreamHandler()
ch.setLevel(logging.INFO)

format_log = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(format_log)
ch.setFormatter(format_log)

logger.addHandler(fh)
logger.addHandler(ch)