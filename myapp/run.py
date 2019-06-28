import logging

from lib_a import aaa
from lib_b import bbb

logging.basicConfig()
logger = logging.getLogger('run')
logger.setLevel(logging.INFO)


print('run.py logging level', logger.getEffectiveLevel())

logger.debug('>run: hello debug')
logger.info('>run: hello info')
logger.warning('>aaa: hello warning')
logger.error('>run: hello error')



if __name__ == '__main__':
    print(f'Logging INFO: {logging.INFO}')