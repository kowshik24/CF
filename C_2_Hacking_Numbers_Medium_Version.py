import sys
 
def ber_kor(command_str):
    print(command_str, flush=True)
 
    # print(command_str, flush=True)
 
    response = sys.stdin.readline().strip()
    # print(response, flush=True)
    if response == "-1":
        sys.exit()
 
def kor():
    n = int(sys.stdin.readline())
   
    # print("!", flush=True)
    # ber_kor("digit")
 
 
    # print("!", flush=True)
    # ber_kor("digit")
    # ber_kor("mul 9")
    # ber_kor(f"add {n-7}")
 
    # ber_kor("digit")
    # ber_kor("mul 9")
    # ber_kor("digit")


    ber_kor("mul 9")
    ber_kor("digit")
    ber_kor("digit")
    ber_kor(f"add {n - 9}")
    
    # ber_kor("mul 9")
    # ber_kor("digit")
    # ber_kor(f"add {n - 9}")
    
    print("!", flush=True)
 
    _ = sys.stdin.readline().strip()


if __name__ == "__main__":
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        kor()