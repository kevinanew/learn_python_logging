import logging

logger = logging.getLogger('lib_a:aaa')

logger.debug('>aaa: hello debug')
logger.info('>aaa: hello info')
logger.warning('>aaa: hello warning')
logger.error('>aaa: hello error')

print('lib_a/aaa.py logging level', logger.getEffectiveLevel())