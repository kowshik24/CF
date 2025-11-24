def kor():
    t = int(input())
    for _ in range(t):
    
        a , b , c = map(int, input().split())
        res = a * b * c
        for i in range(0,6):
            for j in range(0,6):
                for k in range(0,6):
                    if (i + j + k ) == 5:
                        tem = (a + i) * (b + j) * (c + k)
                        # print(f"i = {i} , j = {j} , k = {k} , tem = {tem}")
                        res = max(res,tem)

        
        print(res)




if __name__ == "__main__":
    kor()