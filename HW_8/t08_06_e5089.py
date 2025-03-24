# сортування вставкою
def insertion_sort_lexicographical(words):
    for i in range(1, len(words)):
        key = words[i]
        j = i - 1
        while j >= 0 and words[j] > key:
            words[j + 1] = words[j]
            j -= 1
        words[j + 1] = key
    return words


n = int(input())
words = [input().strip() for _ in range(n)]

sorted_words = insertion_sort_lexicographical(words)

for word in sorted_words:
    print(word)