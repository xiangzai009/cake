import logging
logger=logging.getLogger('logname')
logger.setLevel(logging.DEBUG)

consolelog=logging.StreamHandler()
consolelog.setLevel(logging.INFO)

filelog=logging.FileHandler(filename='../log',encoding='utf-8')
filelog.setLevel(logging.DEBUG)

formatter=logging.Formatter("%(asctime)s|%(levelname)s|%(message)s",datefmt="%Y-%M-%d %H:%M:%S")

logger.addHandler(consolelog)
logger.addHandler(filelog)
consolelog.setFormatter(formatter)
filelog.setFormatter(formatter)