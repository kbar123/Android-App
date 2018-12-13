from Database import Database
import pickle
import os

PATH = r"file_data.txt"


class Pickle(Database):
    def __init__(self):
        Database.__init__(self)

    def set_value(self, key, val):
        if os.stat(PATH).st_size != 0:
            with open(PATH, "rb") as data:
                self.dictionary = pickle.load(data)
        Database.set_value(self, key, val)
        with open(PATH, "wb") as data:
            pickle.dump(self.dictionary, data)

    def get_value(self, key):
        if os.stat(PATH).st_size != 0:
            with open(PATH, "rb") as data:
                self.dictionary = pickle.load(data)
        return Database.get_value(self, key)

    def delete_value(self, key):
        if os.stat(PATH).st_size != 0:
            with open(PATH, "rb") as data:
                self.dictionary = pickle.load(data)
        val = Database.delete_value(self, key)
        with open(PATH, "wb") as data:
            pickle.dump(self.dictionary, data)
        return val