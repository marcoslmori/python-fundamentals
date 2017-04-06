# function3.py

def subtrair(*args): 
	saida = ''
	for a in args:
		saida = saida + str(a)
	print saida


subtrair(2,3,10,50)


def multiplicar (*args, **kwargs):
	print args
	print kwargs
	
	# chamar help
	#print help(kwargs)

multiplicar(2, 3, a=2, b=1, c=4, d=6)

