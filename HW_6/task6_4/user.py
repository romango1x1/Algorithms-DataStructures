size = 100003  # Використовуємо велике просте число для хеш-таблиці
slots = []


def _hash(author: str):
    return sum(ord(c) for c in author) % size


def init():
    global slots
    slots = [None for _ in range(size)]


def addBook(author: str, title: str):
    i = _hash(author)
    if slots[i] is None:
        slots[i] = []
    if title not in slots[i]:
        slots[i].append(title)


def find(author: str, title: str):
    i = _hash(author)
    if slots[i] is None:
        return False
    return title in slots[i]


def delete(author: str, title: str):
    i = _hash(author)
    if slots[i] is not None:
        try:
            slots[i].remove(title)
            if not slots[i]:  # Якщо список книг автора порожній, очищуємо слот
                slots[i] = None
        except ValueError:
            pass


def findByAuthor(author: str):
    i = _hash(author)
    if slots[i] is None:
        return []
    return sorted(slots[i])
