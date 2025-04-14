import sys
sys.setrecursionlimit(1500)


class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = BinaryTree(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = BinaryTree(key)
            else:
                self.right.insert(key)

    def structure(self):
        res = [str(self.key)]
        res += self.left.structure() if self.left else ['#']
        res += self.right.structure() if self.right else ['#']
        return res


def compare_trees(tree1, tree2):
    return tree1.structure() == tree2.structure()


def build_tree(nodes):
    if not nodes:
        return None
    root = BinaryTree(nodes[0])
    for key in nodes[1:]:
        root.insert(key)
    return root


def main():
    input()
    nodes1 = list(map(int, input().split()))
    input()
    nodes2 = list(map(int, input().split()))

    tree1 = build_tree(nodes1)
    tree2 = build_tree(nodes2)

    print(1 if compare_trees(tree1, tree2) else 0)


if __name__ == "__main__":
    main()
    