import datetime
import logging
from random import random
from time import sleep


def wait_until_ok(timeout=5, period=0.25):
    logger = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        logger.warning(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_decorator(orig_func):
    """Creates logs based on docstring"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecor]")
        result = orig_func(*args, **kwargs)
        log.info("%s", orig_func.__doc__)
        return result

    return wrapper


def random_num():
    """Generate random number"""
    return str(random.choice(range(11111, 99999)))
