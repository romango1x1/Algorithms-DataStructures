library = {}


def _hash(author):
    return hash(author) % 1000003


def _probe(index):
    while index in library and library[index][0] is not None:
        index = (index + 1) % 1000003
    return index


def init():
    global library
    library = {}


def addBook(author, title):
    index = _hash(author)
    if index not in library:
        library[index] = (author, [title])
    else:
        if library[index][0] == author:
            if title not in library[index][1]:
                library[index][1].append(title)
        else:
            new_index = _probe(index)
            library[new_index] = (author, [title])


def find(author, title):
    index = _hash(author)
    while index in library:
        if library[index][0] == author and title in library[index][1]:
            return True
        index = (index + 1) % 1000003
    return False


def delete(author, title):
    index = _hash(author)
    while index in library:
        if library[index][0] == author:
            if title in library[index][1]:
                library[index][1].remove(title)
                if not library[index][1]:
                    library[index] = (None, None)
            return
        index = (index + 1) % 1000003


def findByAuthor(author):
    index = _hash(author)
    while index in library:
        if library[index][0] == author:
            return sorted(library[index][1])
        index = (index + 1) % 1000003
    return []
