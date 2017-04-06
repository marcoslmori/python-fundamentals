# function.py
# funcoes - codigos para ser reaproveitados

animais = ['tigre', 'boi', 'galinha']

def exibir_lista(lista):
	# esta importando a variavel animais
	global animais
	for a in lista:
		print a

#exemplo
def printar(string):
	#variavel local
	c= 'c'

	print string


exibir_lista(animais)

