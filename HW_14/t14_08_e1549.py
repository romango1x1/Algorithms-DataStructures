def solve():
    while True:
        line = input().strip()
        if line == '0 0 0':
            break
        n, m, k = map(int, line.split())

        circle = []
        for i in range(1, n + 1):
            circle.append(('G', i))
        for i in range(n + 1, n + m + 1):
            circle.append(('K', i))

        stack = []
        stack.append((circle, 0))  # (current_circle, current_position)

        while len(stack) > 0:
            current_circle, current_pos = stack.pop()

            if len(current_circle) == 1:
                last = current_circle[0]
                print("Gared" if last[0] == 'G' else "Keka")
                break

            first_pos = (current_pos + k - 1) % len(current_circle)
            first_sac = current_circle.pop(first_pos)

            second_pos = (first_pos + k - 1) % len(current_circle)
            second_sac = current_circle.pop(second_pos)

            if first_sac[0] == second_sac[0]:
                new_tribe = 'G'
            else:
                new_tribe = 'K'
            new_id = max(first_sac[1], second_sac[1]) + 1

            current_circle.insert(second_pos, (new_tribe, new_id))

            next_pos = (second_pos + 1) % len(current_circle)

            stack.append((current_circle, next_pos))


solve()
