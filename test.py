import logging

logging.basicConfig(level=logging.DEBUG, filename= "log.log", filemode= "w")


x = 1
y = 2
z = 3

logging.debug("test")
# logging.info()
logging.warning(str(x))
logging.error(str(y))
logging.critical(str(z))