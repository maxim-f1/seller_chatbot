import openai

from time import sleep

import logging


def reconnect(func):
    timeout = 60

    def get_response(*args, **kwargs):
        try:
            logging.debug('Try to connect...')
            return func(*args, **kwargs)
        except openai.error.APIError as e:
            logging.exception(f"OpenAI API returned an API Error: {e}")
            sleep(timeout)
            get_response(*args, **kwargs)
        except openai.error.APIConnectionError as e:
            logging.exception(f"Failed to connect to OpenAI API: {e}")
            sleep(timeout)
            get_response(*args, **kwargs)
        except openai.error.RateLimitError as e:
            logging.exception(e)
            raise f"OpenAI API request exceeded rate limit: {e}"

    return get_response
