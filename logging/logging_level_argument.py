# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug
import logging
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--log", help="set log level")
args = parser.parse_args()
loglevel = args.log

numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
  raise ValueError('Invalid log level: %s' % loglevel)
logging.basicConfig(level=numeric_level)
logger = logging.getLogger()

logger.debug('The level of the logging is %s' % logger.getEffectiveLevel())
logger.info('The level of the logging is %s' % logger.getEffectiveLevel())
logger.warning('The level of the logging is %s' % logger.getEffectiveLevel())
logger.error('The level of the logging is %s' % logger.getEffectiveLevel())
logger.critical('The level of the logging is %s' % logger.getEffectiveLevel())
