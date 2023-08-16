import logging, sys, P_CustomFormatter

logger = logging.getLogger("test")
logger.setLevel(level=logging.DEBUG)


logFileFormatter = logging.Formatter(
    fmt="%(asctime)s, [%(levelname)s], %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
fileHandler = logging.FileHandler(filename=r'./Source/errorlogs.txt', mode="w")
fileHandler.setFormatter(logFileFormatter)
fileHandler.setLevel(level=logging.ERROR)

logStreamFormatter = logging.Formatter(
  fmt="%(asctime)s [%(levelname)s] %(message)s",
  datefmt="%H:%M:%S"
)
consoleHandler = logging.StreamHandler(stream=sys.stdout)
consoleHandler.setFormatter(logStreamFormatter)
consoleHandler.setLevel(level=logging.INFO)
consoleHandler.setFormatter(P_CustomFormatter.CustomFormatter("%(asctime)s [%(levelname)s] %(message)s"))

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

def main():
    logger.debug("test debug")
    logger.info("test info")
    logger.warning("test warning")
    logger.error("test error")

if __name__ == '__main__':
    main()