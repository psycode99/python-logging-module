import logging

module_logger = logging.getLogger('exampleApp.otherMod')


def add(x, y):
    logger = logging.getLogger('exampleApp.otherMod.add')
    try:
        answer = x / y
        logger.info(f' divided {x} by {y} to get {answer}')
    except ZeroDivisionError:
        logger.error(' Zero division Error')
    return x / y
