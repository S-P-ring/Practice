import concurrent.futures
import time


def factorial(finished = 2):
    if finished == 1:
        return 1
    else:
        return factorial(finished-1) * finished

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    t = time.time()
    future1 = executor.submit(factorial, finished=800)
    future2 = executor.submit(factorial, finished=700)
    future3 = executor.submit(factorial, finished=660)
    future4 = executor.submit(factorial, finished=600)
    print(future1.result())
    print(future2.result())
    print(future3.result())
    print(future4.result())
    print(f'Time spend: {time.time() - t}')

with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    t = time.time()
    future1 = executor.submit(factorial, finished=800)
    future2 = executor.submit(factorial, finished=700)
    future3 = executor.submit(factorial, finished=660)
    future4 = executor.submit(factorial, finished=600)
    print(future1.result())
    print(future2.result())
    print(future3.result())
    print(future4.result())
    print(f'Time spend: {time.time() - t}')

if __name__ == '__main__':
    main()
