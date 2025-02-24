import math
import re

EMPTY = None


def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Set:
    M = 31

    def __init__(self, size=1000003):
        self._size = size
        self.count = 0
        self._keys: list[EMPTY | str] = [EMPTY] * size

    def _rehash(self):
        new_size = self._size * 2 + 1
        while not is_prime(new_size):
            new_size += 2

        old_keys = self._keys
        self._size = new_size
        self.count = 0
        self._keys = [EMPTY] * new_size

        for key in old_keys:
            if key is not EMPTY:
                self.add(key)

    def hash(self, s):
        h = 0
        for char in s:
            h = h * self.M + ord(char)
        return h % self._size

    def add(self, key: str):
        if self.count / self._size > 0.7:
            self._rehash()

        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return
            i = (i + 1) % self._size

        self._keys[i] = key
        self.count += 1

    def get(self, key):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return True
            i = (i + 1) % self._size
        return False

    def keys(self):
        return [key for key in self._keys if key is not EMPTY]


def case_1(dict_set: Set, text_set: Set):
    for word in text_set.keys():
        if not dict_set.get(word):
            return False
    return True


def case_2(dict_set: Set, text_set: Set):
    for word in dict_set.keys():
        if not text_set.get(word):
            return False
    return True


if __name__ == "__main__":
    with open("input.txt") as file:
        N, M = map(int, file.readline().split())

        dict_set = Set()
        for _ in range(N):
            word = file.readline().strip().lower()
            dict_set.add(word)

        text_set = Set()
        for _ in range(M):
            line = file.readline().strip().lower()
            line = re.sub(r"[^a-z ]", " ", line)
            for word in line.split():
                if word:
                    text_set.add(word)

    if not case_1(dict_set, text_set):
        print("Some words from the text are unknown.")
    elif not case_2(dict_set, text_set):
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")