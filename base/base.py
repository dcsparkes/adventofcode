# import logging
import pathlib


# from logging.handlers import RotatingFileHandler


# def getLogger(name=__name__, fileName="aoc.log", level=logging.NOTSET):
#     p = pathlib.Path("../log/{}".format(fileName))
#     logger = logging.getLogger(name)
#     logger.setLevel(level)
#     handler = RotatingFileHandler(str(p), maxBytes=2000, backupCount=2)
#     handler.setFormatter(logging.Formatter("%(levelname)-8s %(asctime)s %(name)-12s: %(message)s"))
#     logger.addHandler(handler)
#     return logger


def getInputLines(name, delimiter=None, func=None):
    p = pathlib.Path("../input")
    q = p / name

    with q.open() as inFile:
        for line in inFile:
            if delimiter is None:
                if func:
                    yield func(line.strip())
                else:
                    yield line.strip()
            else:
                for element in line.strip().split(delimiter):
                    if func:
                        yield func(element.strip())
                    else:
                        yield element.strip()


def getInts(fileName):
    with open(fileName) as inFile:
        for line in inFile:
            yield int(line.strip())


def getLines(fileName):
    with open(fileName) as inFile:
        for line in inFile:
            yield line.strip()


def readCSVs(fileName):
    with open(fileName) as inFile:
        for line in inFile:
            for pair in line.strip().split(', '):
                yield pair


if __name__ == '__main__':
    logger = getLogger(__name__, level=logging.DEBUG)
    logger.setLevel("INFO")
    logger.debug('Debug message.')
    logger.info('Info message.')
    logger.warning('Warning message.')
    logger.error('Error message.')
    logger.critical('Critical message.')
