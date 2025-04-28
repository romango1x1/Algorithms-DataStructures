class Graph:
    def __init__(self, matrix):
        self.matrix = matrix

    def counter(self):
        count = 0
        n = len(self.matrix)
        for i in range(n):
            degree = sum(self.matrix[i])
            if degree == 1:
                count += 1
        return count


def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    graph = Graph(matrix)
    print(graph.counter())


if __name__ == "__main__":
    main()
