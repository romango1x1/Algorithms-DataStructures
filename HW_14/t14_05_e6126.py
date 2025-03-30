class Node:
    __slots__ = ['item', 'next']

    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        self._front = None
        self._back = None

    def push(self, n):
        new_node = Node(n)

        if self._front is None:
            self._front = self._back = new_node
        else:
            self._back.next = new_node
            self._back = new_node
        return 'ok'

    def pop(self):
        if self._front is None:
            return 'error'

        value = self._front.item
        self._front = self._front.next
        if self._front is None:
            self._back = None
        return value

    def front(self):
        if self._front is None:
            return 'error'
        return self._front.item

    def size(self):
        def count_nodes(node):
            if node is None:
                return 0
            return 1 + count_nodes(node.next)

        return count_nodes(self._front)

    def clear(self):
        def clear_chain(node):
            if node is None:
                return None
            node.next = clear_chain(node.next)
            return None

        self._front = clear_chain(self._front)
        self._back = None
        return 'ok'

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.strip().split()
        try:
            if method == "push":
                if len(args) != 1:
                    return "error"
                return self.push(int(args[0]))
            elif method in ["pop", "front", "size", "clear", "exit"]:
                if args:
                    return "error"
                return getattr(self, method)()
            else:
                return "error"
        except (ValueError, AttributeError):
            return "error"


if __name__ == '__main__':
    queue = Queue()
    with open("input.txt") as f:
        for line in f:
            res = queue.execute(line)
            print(res)
            if res == "bye":
                break
