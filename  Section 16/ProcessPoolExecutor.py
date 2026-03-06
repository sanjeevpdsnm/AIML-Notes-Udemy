from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number : {number}"
numbers = [1,2,3,4,5,6]

with ThreadPoolExecutor(max_workers=6) as executor:
    results = executor.map(print_number,numbers)
    start = time.time()
    for result in results:
        print(result)
    end = time.time()
    print("Total Time: ", end - start)