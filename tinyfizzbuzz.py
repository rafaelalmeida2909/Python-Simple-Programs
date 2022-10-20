def fb(num: int = 100):
	for i in range(1, num+1):
		print(f"{i} {'Fizz' if i % 3 == 0 else ''}{'Buzz' if i % 5 == 0 else ''}")

if __name__ == "__main__":
	fb()
	
