def solve_kor():
    import sys
    input = sys.stdin.readline
    test_cases = int(input())
    results = []

    for _ in range(test_cases):
        total_elements, players, k = map(int, input().split())

        num1 = total_elements // (players + 1)
        num2 = total_elements - players * k
        max_number = min(num1, num2)

        array = [max_number] * total_elements

        for index in range(max_number):
            left = index
            right = total_elements - max_number + index
            #print("righ is: ", right)

            baki_ase = right - left
            #print("baki ase: ", baki_ase)
            count_num = max(1, baki_ase // players)

            for p1 in range(players + 1):
                pos = left + p1 * count_num
                #print("pos:", pos)
                if pos > right:
                    pos = right
                array[pos] = index

        results.append(" ".join(map(str, array)))

    print("\n".join(results))


if __name__ == "__main__":
    solve_kor()
