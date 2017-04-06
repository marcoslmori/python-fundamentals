# function2.py

animais = ['tigre', 'boi', 'galinha']

def exibir_lista(lista):
	# esta importando a variavel animais
	global animais
	for a in lista:
		print a

#exemplo
# parametro opcional
#def somar(a,b=2): se passar o valor sera subscrito
# na declaracao resultado = somar (b=2, a=4)


def somar(a,b):
	return a+b
	

print '--------------------------'

exibir_lista(animais)

print '--------------------------'

print somar (2,2)

print '--------------------------'
a=int(raw_input('Valor a: '))
b=int(raw_input('Valor b: '))

resultado = somar(a, b)
print resultado
# dando erro checar
