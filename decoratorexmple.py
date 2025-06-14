import logging
from functools import wraps

# Logger setup
logging.basicConfig(level=logging.INFO)

def log_test_case(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Starting test: {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Finished test: {func.__name__}")
        return result
    return wrapper

# Example usage in a test case
@log_test_case
def test_login():
    # Login test logic
    assert True
