# funcao_lambda.py
# funcoes anonimas

f = lambda x,y,z: x + y + z

print f(2,3,4)

words = ('pera', 'uva', 'mamao')


def size(words):
	return [len(w) for w in words]

print size(words)


# transformando em lambda

frutas = lambda words: [len(w) for w in words]
frutas(words)

print frutas(words)


# outra forma de fazer a funcao acima

def size(words):
	lista = []
	for w in words:
		lista.append(w)
	return lista

frutas2 = lambda words: [len(w) for w in words]


print frutas2(words)