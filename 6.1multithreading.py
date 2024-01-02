# Write a program to implement Multithreading. Printing “Hello” with one thread & printing “Hi” with another thread.

import threading

def print_hello():
    for _ in range(5):
        print("Hello")

def print_hi():
    for _ in range(5):
        print("Hi")

thread_hello = threading.Thread(target=print_hello)
thread_hi = threading.Thread(target=print_hi)

thread_hello.start()
thread_hi.start()

thread_hello.join()
thread_hi.join()
