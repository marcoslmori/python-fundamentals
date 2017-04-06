#tryexcept.py

# def func():
#	pass

try:
	print 'primeira linha'
	func()
	a = 3 + 3
	
except Exception as e:
	print e 
	print 'algo de errado aconteceu'



print '-------------------------'

def func(valor):
	if valor:
		raise Exception('Deu ruim!!')

try:
	print 'primeira linha'
	func(True)
	print  3 + 3
	
except Exception as e:
	print e 



print '-----Finally--------------------'

def func(valor):
	if valor:
		raise Exception('Deu ruim!!')

try:
	print 'primeira linha'
	func(True)
	print  3 + 3
	
except Exception as e:
	print e 

finally:
	print 'sempre executa'
