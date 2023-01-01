import logging
import otherMod
import logging.config
import dictConfig


def main():
    logging.config.dictConfig(dictConfig.dictLogConfig)
    logger = logging.getLogger('exampleApp')
    logger.info("Program started")

    try:
        otherMod.add(10, 0)
    except NameError:
        logger.error(' Name Error!!!')
    else:
        logger.info("Division Successfully Done!")


if __name__ == '__main__':
    main()
