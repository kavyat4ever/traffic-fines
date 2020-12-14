class MyHashTable:

    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def set(self, key, value):
        slot = hash(key) % self.size
        while self.keys[slot] and self.keys[slot] != key:
            slot = hash(slot + 1) % self.size
        self.keys[slot] = key
        self.values[slot] = value

    def get(self, key):
        return self.values[self.get_slot(key)]

    def destroy(self):
        self.keys = None
        self.values = None
        self.size = 0

