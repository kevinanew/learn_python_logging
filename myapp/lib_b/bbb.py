import logging

logger = logging.getLogger('lib_b:bbb')
logger.setLevel(logging.ERROR)

logger.debug('>bbb: hello debug')
logger.info('>bbb: hello info')
logger.warning('>bbb: hello warning')
logger.error('>bbb: hello error')


print('lib_b/bbb.py logging level', logger.getEffectiveLevel())