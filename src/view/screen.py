import os
import threading
import time


def run():
    t1 = threading.Thread(target=loop, args=('test',))
    t1.start()
    t2 = threading.Thread(target=spinner)
    t2.start()


def loop(print_screen: str):
    while True:
        print(print_screen)
        user_input()
        os.system('clear')


def spinner():
    spinner = ['/', '|', '\\', '-']
    for char in spinner:
        print(char)


def user_input():
    return input('=>')
