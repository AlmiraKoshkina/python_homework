# TASK 1: Decorator with logging

import logging

# Logger setup (one-time configuration)
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


# Define the logger_decorator
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        func_name = func.__name__
        pos_args = args if args else "none"
        kw_args = kwargs if kwargs else "none"

        log_message = (
            f"function: {func_name}\n"
            f"positional parameters: {pos_args}\n"
            f"keyword parameters: {kw_args}\n"
            f"return: {result}\n"
        )

        logger.info(log_message)
        return result
    return wrapper


# --- Test functions ---

# 1. Function with no parameters
@logger_decorator
def say_hello():
    print("Hello, World!")


# 2. Function with positional arguments
@logger_decorator
def accept_args(*args):
    print("Got positional args:", args)
    return True


# 3. Function with keyword arguments
@logger_decorator
def accept_kwargs(**kwargs):
    print("Got keyword args:", kwargs)
    return logger_decorator


# --- Main block to call the functions ---
if __name__ == "__main__":
    say_hello()
    accept_args(1, 2, 3)
    accept_kwargs(name="Alex", age=23)
