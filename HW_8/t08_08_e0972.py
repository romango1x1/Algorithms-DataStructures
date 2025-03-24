# сортування вибором
def selection_sort_time(moments):
    n = len(moments)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if (moments[j][0] < moments[min_idx][0]) or \
               (moments[j][0] == moments[min_idx][0] and moments[j][1] < moments[min_idx][1]) or \
               (moments[j][0] == moments[min_idx][0] and moments[j][1] == moments[min_idx][1] and moments[j][2] < moments[min_idx][2]):
                min_idx = j
        moments[i], moments[min_idx] = moments[min_idx], moments[i]
    return moments


n = int(input())
moments = []
for _ in range(n):
    h, m, s = map(int, input().split())
    moments.append((h, m, s))

sorted_moments = selection_sort_time(moments)

for moment in sorted_moments:
    print(moment[0], moment[1], moment[2])