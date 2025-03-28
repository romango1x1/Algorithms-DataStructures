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

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")
        item = self.top.item
        self.top = self.top.next
        self._size -= 1
        return item

    def back(self):
        if self.top is None:
            raise IndexError("peek from empty stack")
        return self.top.item

    def is_empty(self):
        return self.top is None

    def size(self):
        return self._size


def backtrack(current, remaining, stack, result):
    if remaining == 0:
        if stack.is_empty():
            result.append(''.join(current))
        return

    for open_bracket in ['(', '[']:
        stack.push(open_bracket)
        backtrack(current + [open_bracket], remaining - 1, stack, result)
        stack.pop()

    if not stack.is_empty():
        try:
            last = stack.back()
            if last == '(':
                stack.pop()
                backtrack(current + [')'], remaining - 1, stack, result)
                stack.push('(')
            elif last == '[':
                stack.pop()
                backtrack(current + [']'], remaining - 1, stack, result)
                stack.push('[')
        except IndexError:
            pass


def generate_parentheses(n, stack_class):
    result = []
    stack = stack_class()
    backtrack([], n, stack, result)
    return result


def main():
    n = int(input())
    for seq in generate_parentheses(n, Stack):
        print(seq)


if __name__ == "__main__":
    main()
