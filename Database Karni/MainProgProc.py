# -*- coding: utf-8 -*-
from Sync import Sync
import threading
SYNC_PROCESS = Sync(False)
KEYS = ["karni", "bar", "ely", "shaffir", "ronny", "baranetz",
        "aviv", "doyev", "tamar", "sadot", "inbar", "rousso", "ori", "sharabi"]

VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def set_process(key, value):
    Sync.set_value(SYNC_PROCESS, key, value)


def delete_process(key):
    Sync.delete_value(SYNC_PROCESS, key)


def get_process(key):
    print Sync.get_value(SYNC_PROCESS, key)


def create_set_process(num, key, value):
    set_threads = []
    for i in range(num):
        set_threads.append(threading.Thread
                           (target=set_process(key[i], value[i])))
    return set_threads


def create_get_process(num, key):
    get_threads = []
    for i in range(num):
        get_threads.append(threading.Thread(target=get_process, args=(key[i],)))
    return get_threads


def create_delete_process(num, key):
    delete_threads = []
    for i in range(num):
        delete_threads.append(threading.Thread(target=delete_process(key[i])))
    return delete_threads


def main():
    while True:
        p_list = create_set_process(14, KEYS, VALUES)
        for p in p_list:
            p.start()
        create_get_process(14, KEYS)

if __name__ == '__main__':
    main()
