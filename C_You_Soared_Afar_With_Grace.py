import sys
import math
from collections import defaultdict

def main():
    inp = sys.stdin.read().split()
    oii = iter(inp)

    num1 = int(next(oii))
    final_res = []

    for _ in range(num1):
        kos = int(next(oii))
        ber_kor = [int(next(oii)) for _ in range(kos)]
        kire = [int(next(oii)) for _ in range(kos)]

        num_list = defaultdict(list)

        for num2 in range(kos):
            num_list[(ber_kor[num2], kire[num2])].append(num2)

        flag = True
        tem_num = None
        kos_number = []

        for (num3, num4) in list(num_list.keys()):
            if num3 != num4 and (num3, num4) in num_list and (num4, num3) in num_list and num3 < num4:
                if len(num_list[(num3, num4)]) != len(num_list[(num4, num3)]):
                    flag = False
                    break
                num5 = len(num_list[(num3, num4)])
                for num6 in range(num5):
                    kos_number.append((num_list[(num3, num4)][num6], num_list[(num4, num3)][num6]))

        if not flag:
            #print("continue")
            final_res.append("-1")
            continue

        for (num3, num4) in list(num_list.keys()):
            if num3 == num4:
                res_num1 = num_list[(num3, num4)]
                num5 = len(res_num1)
                num7 = num5 // 2
                #print("num5", num7)
                for num6 in range(num7):
                    kos_number.append((res_num1[num6], res_num1[num6 + num7]))
                if num5 % 2 == 1:
                    if tem_num is None:
                        tem_num = res_num1[-1]
                    else:
                        flag = False
                        break

        if not flag:
            final_res.append("-1")
            continue

        total = 2 * len(kos_number) + (1 if tem_num is not None else 0)
        #print("total", total)

        if total != kos:
            final_res.append("-1")
            continue

        kos_number.sort(key=lambda x: x[0])

        right_number = [p[0] for p in kos_number]
        left_number = [p[1] for p in kos_number]
        left_number.reverse()

        merged = right_number + ([tem_num] if tem_num is not None else []) + left_number

        #print("merged", merged)

        mapped_list = list(range(kos))
        index_pos = [0] * kos

        for num2 in range(kos):
            index_pos[mapped_list[num2]] = num2

        final_result = []

        for num2 in range(kos):
            if mapped_list[num2] == merged[num2]:
                continue
            num8 = index_pos[merged[num2]]
            mapped_list[num2], mapped_list[num8] = mapped_list[num8], mapped_list[num2]
            index_pos[mapped_list[num2]] = num2
            index_pos[mapped_list[num8]] = num8
            final_result.append((num2, num8))

        if len(final_result) > kos:
            final_res.append("-1")
        else:
            final_res.append(str(len(final_result)))
            for num9, num10 in final_result:
                final_res.append(f"{num9 + 1} {num10 + 1}")

    sys.stdout.write("\n".join(final_res))

if __name__ == "__main__":
    main()
