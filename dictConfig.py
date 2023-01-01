dictLogConfig = {
        'version': 1,
        'handlers': {
            'fileHandler': {
                'class': 'logging.FileHandler',
                'formatter': 'myFormatter',
                'filename': 'config2.log'
            }
        },
        'loggers': {
            'exampleApp': {
                'handlers': ['fileHandler'],
                'level': 'INFO'
            }
        },
        'formatters': {
            'myFormatter': {
                'format': '%(asctime)s-%(name)s-%(levelname)s-%(message)s'
            }
        }
    }