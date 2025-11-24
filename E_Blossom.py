def solve():

    import sys

    data = sys.stdin.read().strip().split()

    if not data: 

        return

    t = int(data[0])

    index = 1

    out_lines = []

    

    for _ in range(t):

        n = int(data[index])
        m = int(data[index+1])
        k = int(data[index+2])

        index += 3

        #T1 = n if m == -1 else n // (m + 1)
        T1 = n // (m+1)

        T2 = n - m * k

        T = min(T1, T2)

        ans = [T] * n

        for x in range(T):

            L = x

            R = n - T + x

            gap = R - L

            step = gap // m if m != 0 else 0

            for j in range(m + 1):

                pos = L + j * step

                if pos > R:

                    pos = R

                ans[pos] = x

        out_lines.append(" ".join(map(str, ans)))

    

    sys.stdout.write("\n".join(out_lines))



if __name__ == "__main__":

    solve()