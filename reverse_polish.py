#Calculadora polonesa inversa

pilha = []

iniciar = int(input('Digite 1 p/ iniciar a calculadora: '))

#recebe os valores, ou operação e os adiciona na pilha
while iniciar == 1:
	valores = input('Número ou operação (digite "sair" p/ sair): ')  #As operações e a opção de sair tem que ser passadas como string
	pilha.append(valores)
	topo = len(pilha)

	#A pilha aqui é lida de forma inversa com o "[-1]", as operações
	#são feitas simultaneamente de acordo com os condicionais e adicionados em 
	#seguida na pilha.
	
	if pilha[-1] == '*':
		x = float(pilha[topo-2])
		y = float(pilha[topo-3])
		val1 = x
		val2 = y
		if val1 > val2:
			op = val1*val2
		else:
			op = val2*val1
		pilha.pop()
		pilha.pop()
		pilha.pop()
		pilha.append(op)
	if pilha[-1] == '/':
		x = float(pilha[topo-2])
		y = float(pilha[topo-3])
		val1 = x
		val2 = y
		if val1 > val2:
			op = val1/val2
		else:
			op = val2/val1
		pilha.pop()
		pilha.pop()
		pilha.pop()
		pilha.append(op)
	if pilha[-1] == '+':
		x = float(pilha[topo-2])
		y = float(pilha[topo-3])
		val1 = x
		val2 = y
		if val1 > val2:
			op = val1+val2
		else:
			op = val2+val1
		pilha.pop()
		pilha.pop()
		pilha.pop()
		pilha.append(op)
	if pilha[-1] == '-':
		x = float(pilha[topo-2])
		y = float(pilha[topo-3])
		val1 = x
		val2 = y
		if val1 > val2:
			op = val1 - val2
		else:
			op = val2 - val1
		pilha.pop()
		pilha.pop()
		pilha.pop()
		pilha.append(op)

	#Tira o ultimo elemento da pilha que seria a string "sair" e printa
	#o conteúdo da pilha.

	if valores == 'sair':
		pilha.pop()
		print(pilha)
		break


