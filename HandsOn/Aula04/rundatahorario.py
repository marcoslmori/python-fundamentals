#rundatahorario.py

from datetime import datetime, timedelta
#timedelta consegue guardar o periodo de um tempo

print datetime.now()
print '-----------------------'
print datetime.now().hour
print '-----------------------'
# https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime
print datetime.now().strftime('%H - %d - %b')
print '-----------------------'
print datetime(1990, 8, 1, 0,0,0)
print '-----------------------'
print datetime(1990, 8, 1, 0,0,0).strftime('%d/%b/%Y')
print '-----------------------'
# O resultado eh o data atual mais 4 dias do timedelta
print datetime.now() + timedelta(4)
print '-----------------------'
print timedelta(4)
print '-----------------------'
print datetime.now() + timedelta(hours=3)
print '-----------------------'
print datetime.now() + timedelta(
	days=4,
	seconds=1231,
	milliseconds=123,
	minutes=21,
	hours=4,
	weeks=1
 )
print '-----------------------'

data1 = datetime(1990, 8, 1, 0,0,0)
data2 = datetime(1990, 8, 1, 0,1,0)

if (data1 - data2).total_seconds() > 3600:
	print 'prazo expirado'
else:
	print 'dentro do prazo'

	




