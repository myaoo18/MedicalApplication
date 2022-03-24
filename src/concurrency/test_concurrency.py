from . import concurrency

# Tests the order_in_given_multithreading_method
def test_order_in_given_multithreading_method() -> None:
    seconds_to_sleep = [5, 4, 3, 2, 1]
    duration = concurrency.order_in_given_multithreading_method(seconds_to_sleep)
    assert duration < 5.2


# Tests the order_in_completed_multithreading_method
def test_order_in_completed_multithreading_method() -> None:
    seconds_to_sleep = [5, 4, 3, 2, 1]
    duration = concurrency.order_in_completed_multithreading_method(seconds_to_sleep)
    assert duration < 5.2
