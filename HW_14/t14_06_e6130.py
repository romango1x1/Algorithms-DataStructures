class Node:
    __slots__ = ['value', 'next', 'prev']

    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Deque:
    def __init__(self, front=None, back=None, size=0):
        self.front = front
        self.back = back
        self.size = size

    def push_front(self, value):
        if self.front is None:
            new_node = Node(value)
            return Deque(new_node, new_node, 1)
        new_node = Node(value, next=self.front)
        self.front.prev = new_node
        return Deque(new_node, self.back, self.size + 1)

    def push_back(self, value):
        if self.back is None:
            new_node = Node(value)
            return Deque(new_node, new_node, 1)
        new_node = Node(value, prev=self.back)
        self.back.next = new_node
        return Deque(self.front, new_node, self.size + 1)

    def pop_front(self):
        if self.front is None:
            return self, "error"
        value = self.front.value
        new_front = self.front.next
        if new_front is None:
            return Deque(None, None, 0), value
        new_front.prev = None
        return Deque(new_front, self.back, self.size - 1), value

    def pop_back(self):
        if self.back is None:
            return self, "error"
        value = self.back.value
        new_back = self.back.prev
        if new_back is None:
            return Deque(None, None, 0), value
        new_back.next = None
        return Deque(self.front, new_back, self.size - 1), value

    def get_front(self):
        if self.front is None:
            return "error"
        return str(self.front.value)

    def get_back(self):
        if self.back is None:
            return "error"
        return str(self.back.value)

    def get_size(self):
        return str(self.size)

    def clear(self):
        return Deque(None, None, 0)

    def process_command(self, command):
        parts = command.split()
        if not parts:
            return self, ""

        cmd = parts[0]

        if cmd == "push_front":
            if len(parts) != 2:
                return self, "error"
            try:
                value = int(parts[1])
                new_deque = self.push_front(value)
                return new_deque, "ok"
            except ValueError:
                return self, "error"

        elif cmd == "push_back":
            if len(parts) != 2:
                return self, "error"
            try:
                value = int(parts[1])
                new_deque = self.push_back(value)
                return new_deque, "ok"
            except ValueError:
                return self, "error"

        elif cmd == "pop_front":
            if len(parts) != 1:
                return self, "error"
            new_deque, result = self.pop_front()
            return new_deque, str(result)

        elif cmd == "pop_back":
            if len(parts) != 1:
                return self, "error"
            new_deque, result = self.pop_back()
            return new_deque, str(result)

        elif cmd == "front":
            if len(parts) != 1:
                return self, "error"
            return self, self.get_front()

        elif cmd == "back":
            if len(parts) != 1:
                return self, "error"
            return self, self.get_back()

        elif cmd == "size":
            if len(parts) != 1:
                return self, "error"
            return self, self.get_size()

        elif cmd == "clear":
            if len(parts) != 1:
                return self, "error"
            new_deque = self.clear()
            return new_deque, "ok"

        elif cmd == "exit":
            if len(parts) != 1:
                return self, "error"
            return self, "bye"

        else:
            return self, "error"


def main():
    deque = Deque()
    while True:
        try:
            command = input().strip()
            if not command:
                continue

            deque, result = deque.process_command(command)
            print(result)

            if result == "bye":
                break
        except EOFError:
            print("bye")
            break


if __name__ == "__main__":
    main()
