def ber_kor():
	t = int(input())
	while t > 0:
		n = int(input())
		if n % 2 == 1:
			print(0)
		else:
			print(n // 4 + 1)
		t -= 1


if __name__ == "__main__":
	ber_kor()
