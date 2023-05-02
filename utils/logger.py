import config

import logging
import logging.config
import logging.handlers

import json


LOGGER = logging.getLogger('main.moduls.utils.logger')


class Logger:
    __instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in Logger.__instance:
            Logger.__instance[cls] = super().__new__(cls)
        return Logger.__instance[cls]

    @staticmethod
    def init_logging():
        logging.config.dictConfig(Logger._get_log_config())
        LOGGER.debug(config.SETTINGS['logger_init'])

    @staticmethod
    def _get_log_config() -> dict:
        with open(config.LOGGER_CONFIG_PATH, 'r') as config_file:
            return json.load(config_file)
