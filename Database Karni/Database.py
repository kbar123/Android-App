class Database():
    def __init__(self):
        self.dictionary = {}

    def set_value(self, key, val):
        self.dictionary[key] = val
        return True

    def get_value(self, key):
        if key in self.dictionary:
            return self.dictionary[key]
        else:
            return None

    def delete_value(self, key):
        return self.dictionary.pop(key, None)
