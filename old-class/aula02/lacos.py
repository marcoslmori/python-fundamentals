#lacos.py

i = 0

while i < 10:
	print i
	i += 1


print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

i = 0 

while i < 10:
	if i == 5: 
		#break
		i += 1
		continue
	print i
	i += 1

print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

for value in ['pera','uva', 'banana']:
	print value


print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

for value in ['pera','uva', 'banana']:
	if value == 'uva':
		continue
	print value

print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

for value in 'PYTHON':
	print value


print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

for value in 'PYTHON':
	if value == 'T':
		continue
	print value


print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

for value in 'PYTHON':
	if value == 'T':
		continue
	print value
else:
	print 'Close a conexao'


print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

animais  = ['gato', 'cachorro', 'passarinho']
animais.append('boi')
print animais


print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

animais  = ['gato', 'cachorro', 'passarinho']
animais.append('boi')
print animais
animais.insert(1, 'tigre')
print animais

print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

animais  = ['gato', 'cachorro', 'passarinho']
animais.append('boi')
print animais
animais.insert(1, 'tigre')
print animais
animais.remove('gato')
print animais
#retira o ultimo da lista 
animais.pop()
print animais


print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

animais  = ['gato', 'cachorro', 'passarinho']
animais.append('boi')
print animais
animais.insert(1, 'tigre')
print animais
animais.remove('gato')
print animais
#retira o ultimo da lista 
animais.pop()
print animais
animais.count('tigre')
print animais

print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

animais  = ['gato', 'cachorro', 'passarinho']
animais.append('boi')
print animais
animais.insert(1, 'tigre')
print animais
animais.remove('gato')
print animais
#retira o ultimo da lista 
animais.pop()
print animais
print animais.count('tigre')
print animais
print len(animais)


print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

animais  = ['gato', 'cachorro', 'passarinho']
animais.append('boi')
print animais
animais.insert(1, 'tigre')
print animais
animais.remove('gato')
print animais
#retira o ultimo da lista 
animais.pop()
print animais
print animais.count('tigre')
print animais
print len(animais)

if 'tigre' in animais:
	print 'encontrei o tigre'

print 'xxxxxxxxxxxxxxxxxxxxxxxxx'

animais  = ['gato', 'cachorro', 'passarinho']
animais.append('boi')
print animais
animais.insert(1, 'tigre')
print animais
animais.remove('gato')
print animais
#retira o ultimo da lista 
animais.pop()
print animais
print animais.count('tigre')
print animais
print len(animais)
print animais.index('tigre')
animais.reverse()
print animais
if 'tigre' in animais:
	print 'encontrei o tigre'
