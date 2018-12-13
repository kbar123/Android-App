# -*- coding: utf-8 -*-
from Sync import Sync
import threading
SYNC_THREAD = Sync(True)
KEYS = ["karni", "bar", "ely", "shaffir", "ronny", "baranetz",
        "aviv", "doyev", "tamar", "sadot", "inbar", "rousso", "ori", "sharabi"]

VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def set_thread(key, value):
    Sync.set_value(SYNC_THREAD, key, value)


def delete_thread(key):
    Sync.delete_value(SYNC_THREAD, key)


def get_thread(key):
    print Sync.get_value(SYNC_THREAD, key)


def create_set_threads(num, key, value):
    set_threads = []
    for i in range(num):
        set_threads.append(threading.Thread
                           (target=set_thread(key[i], value[i])))
    return set_threads


def create_get_threads(num, key):
    get_threads = []
    for i in range(num):
        get_threads.append(threading.Thread(target=get_thread(key[i])))
    return get_threads


def create_delete_threads(num, key):
    delete_threads = []
    for i in range(num):
        delete_threads.append(threading.Thread(target=delete_thread(key[i])))
    return delete_threads


def main():
    while True:
        create_get_threads(14, KEYS)
        create_set_threads(14, KEYS, VALUES)

if __name__ == '__main__':
    main()
