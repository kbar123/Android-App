# -*- coding: utf-8 -*-
from Pickle import Pickle
import threading
import multiprocessing
import logging
SEMAPHORE_MAX_NUM = 10


class Sync(Pickle):
    def __init__(self, thread):
        logging.basicConfig(filename='logging.log', level=logging.DEBUG,
                            format='%(asctime)s %(message)s')
        if thread:
            self.my_lock = threading.Lock()
            self.my_semaphore = threading.Semaphore(SEMAPHORE_MAX_NUM)
        else:
            self.my_lock = multiprocessing.Lock()
            self.my_semaphore = multiprocessing.Semaphore(SEMAPHORE_MAX_NUM)
        Pickle.__init__(self)

    def set_value(self, key, val):
        logging.info("writing to database")
        self.my_lock.acquire()
        for i in range(SEMAPHORE_MAX_NUM):
            self.my_semaphore.acquire()
        Pickle.set_value(self, key, val)
        for i in range(SEMAPHORE_MAX_NUM):
            self.my_semaphore.release()
        self.my_lock.release()
        logging.info("finished writing to database")

    def delete_value(self, key):
        logging.info("deleting from database")
        self.my_lock.acquire()
        for user in range(SEMAPHORE_MAX_NUM):
            self.my_semaphore.acquire()
        Pickle.delete_value(self, key)
        for user in range(SEMAPHORE_MAX_NUM):
            self.my_semaphore.release()
        self.my_lock.release()
        logging.info("finished deleting from database")

    def get_value(self, key):
        logging.info("reading from database")
        self.my_semaphore.acquire()
        val = Pickle.get_value(self, key)
        self.my_semaphore.release()
        logging.info("finished reading from database")
        return val

if __name__ == '__main__':
    pass
