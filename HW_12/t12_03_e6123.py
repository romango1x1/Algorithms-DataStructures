class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node
        self._size += 1
        return "ok"

    def pop(self):
        if self.top is None:
            return "error"
        item = self.top.item
        self.top = self.top.next
        self._size -= 1
        return item

    def back(self):
        if self.top is None:
            return "error"
        return self.top.item

    def clear(self):
        self.top = None
        self._size = 0
        return "ok"

    def size(self):
        return self._size

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    stack = Stack()
    while True:
        line = input().strip()
        if not line:
            continue
        result = stack.execute(line)
        print(result)
        if line.split()[0] == "exit":
            break