#task2
user = raw_input('Username: ')
pswd = raw_input('Password: ')

userval = 'arthur.dent'
pswdval = 'mochileiro'

if user == userval and pswd == pswdval:
	print 'usuario autenticado com sucesso'
	print 'Seja bem-vindo, %s' %user
else:
	print 'acesso negado'

