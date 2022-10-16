n=num//2
while n<=num:
	if n+int(str(n)[::-1])==num:
		return True
	n+=1
return False
