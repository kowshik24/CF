def ber_kor(x, y, s):
    if s == 2:
        if x == 1 and y == 1:
            return 1
        elif x == 2 and y == 2:
            return 2
        elif x == 2 and y == 1:
            return 3
        else:
            return 4
    res = s // 2
    # print(f"res: {res}")
    if x <= res and y <= res:
        new_x, new_y = x, y
        temp = 0
    elif x > res and y > res:
        new_x, new_y = x - res, y - res
        # print(f"new_x: {new_x}, new_y: {new_y}")
        temp = (res ** 2) * 1
    elif x > res:
        new_x, new_y = x - res, y
        # print(f"new_x: {new_x}, new_y: {new_y}")
        temp = (res ** 2) * 2
    else:
        new_x, new_y = x, y - res
        # print(f"new_x: {new_x}, new_y: {new_y}")
        temp = (res ** 2) * 3

    #print(f"x: {x}, y: {y}, s: {s}, new_x: {new_x}, new_y: {new_y}, temp: {temp}")
    return temp + ber_kor(new_x, new_y, res)

def solve_kor(d, s):
    if s == 2:
        if d == 1:
            return (1, 1)
        elif d == 2:
            return (2, 2)
        elif d == 3:
            return (2, 1)
        else:
            return (1, 2)
        

    res = s // 2
    total = res ** 2
    # print(f"res: {res}, total: {total}")
    if d <= total:
        temp_kos = 0
        new_d = d
    elif d <= 2 * total:
        temp_kos = 1
        new_d = d - total
        # print(f"temp_kos: {temp_kos}, new_d: {new_d}")
    elif d <= 3 * total:
        temp_kos = 2
        new_d = d - 2 * total
        # print(f"temp_kos: {temp_kos}, new_d: {new_d}")
    else:
        temp_kos = 3
        new_d = d - 3 * total
        # print(f"temp_kos: {temp_kos}, new_d: {new_d}")
    x, y = solve_kor(new_d, res)
    # print(f"temp_kos: {temp_kos}, new_d: {new_d}, x: {x}, y: {y}")
    if temp_kos == 0:
        return (x, y)
    elif temp_kos == 1:
        return (x + res, y + res)
    elif temp_kos == 2:
        return (x + res, y)
    else:
        return (x, y + res)

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        q = int(input[ptr])
        ptr += 1
        s = 2 ** n
        for __ in range(q):
            partition = input[ptr:ptr+3] if input[ptr] == '->' else input[ptr:ptr+2]
            # print(partition)
            ptr += len(partition)
            if partition[0] == '->':
                x = int(partition[1])
                y = int(partition[2])
                print(ber_kor(x, y, s))
            else:
                d = int(partition[1])
                x, y = solve_kor(d, s)
                print(x, y)

if __name__ == '__main__':
    main()