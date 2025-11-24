def solve_me(test_case):
    s = input().strip()
    ss = input().strip()
    n = len(s)
    m = len(ss)
    j = 0
    s_list = list(s)  # Convert s to a list for mutability

    for i in range(n):
        if s_list[i] == '?' and j < m:
            s_list[i] = ss[j]
            j += 1
        elif s_list[i] == '?':
            s_list[i] = 'a'
        elif j < m and s_list[i] == ss[j]:
            j += 1

    s = ''.join(s_list)  # Convert list back to string

    if j == m:
        print("YES")
        print(s)
    else:
        print("NO")

def main():
    test_cases = int(input().strip())
    for _ in range(test_cases):
        solve_me(_)

if __name__ == "__main__":
    main()