def merge_sort(robots):
    if len(robots) <= 1:
        return robots

    mid = len(robots) // 2
    left = merge_sort(robots[:mid])
    right = merge_sort(robots[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]:
            result.append(right[j])
            j += 1
        else:
            if left[i][2] < right[j][2]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


n = int(input())
robots = []
for idx in range(n):
    main, auxiliary = map(int, input().split())
    robots.append((main, auxiliary, idx))

sorted_robots = merge_sort(robots)

for robot in sorted_robots:
    print(robot[0], robot[1])