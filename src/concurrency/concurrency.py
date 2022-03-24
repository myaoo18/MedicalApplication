import concurrent.futures
import time
# This program runs threads concurrently using the threading module.

def sleeper(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping... {seconds}'

def order_in_given_multithreading_method(seconds_to_sleep):
    # Multithreading method to run threads in the order that's given

    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(sleeper, seconds_to_sleep)

        # Print out results as the order that's given
        for result in results:
            print(result)
    finish = time.perf_counter()
    duration = finish - start
    return duration

def order_in_completed_multithreading_method (seconds_to_sleep):
    # Multithreading method to run threads in the order that's completed

    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submitting each value in seconds_to_sleep 
        results = [executor.submit(sleeper, sec) for sec in seconds_to_sleep]

        # Print out results as the order that it's completed
        for f in concurrent.futures.as_completed(results):
            print(f.result())
    finish = time.perf_counter()
    duration = finish - start
    return duration

if __name__ == "__main__":

    # Multithreading order in the order that is given
    seconds_to_sleep = [5, 4, 3, 2, 1]
    print (f'Starting order given multithreading module with sleep times {seconds_to_sleep} second(s)')
    duration = order_in_given_multithreading_method(seconds_to_sleep)
    print (f'Finished order given multithreading in {round(duration,2)} second(s)')
    
    print('')

    # Multithreading order in the order that is completed
    print (f'Starting order completed multithreading module with sleep times {seconds_to_sleep} second(s)')
    duration = order_in_completed_multithreading_method(seconds_to_sleep)
    print (f'Finished order compelted multithreading in {round(duration,2)} second(s)')