t = int(input())

for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    suneet_wins = 0

    combinations = [
        (a1, b1, a2, b2),
        (a1, b2, a2, b1),
        (a2, b1, a1, b2),
        (a2, b2, a1, b1)
    ]

    for a_first, b_first, a_second, b_second in combinations:
        suneet_rounds = 0
        slavic_rounds = 0

        if a_first > b_first:
            suneet_rounds += 1
        elif a_first < b_first:
            slavic_rounds += 1

        if a_second > b_second:
            suneet_rounds += 1
        elif a_second < b_second:
            slavic_rounds += 1

        if suneet_rounds > slavic_rounds:
            suneet_wins += 1

    print(suneet_wins)