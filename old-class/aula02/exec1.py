# exec1.py

alcool = raw_input('Esta alcoolizada?(S/N): ').upper() 
idade = raw_input('Digite a sua idade: ')
if idade is None: 
	idade = 5
	print 'idade'
habilitacao = raw_input('Tem Habilitacao?(S/N): ').upper()

if alcool == 'S':
	print 'Proibida de dirigir'
else:
	if int(idade) >= 18:
		print 'OK, pode dirigir'
	elif habilitacao == 'S':
		print 'OK, pode dirigir'
	else: 
		print 'nao pode dirigir'

# forma mais enchuta
#if idade >= 18 and habilitacao == 'S' and alcool == 'N':
#	 print 'Pode dirigir'
#	else:
#		print 'Nao pode dirigir'





