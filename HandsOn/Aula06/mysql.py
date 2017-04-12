# mysql
import MySQLdb
con = MySQLdb.connect(
		host='127.0.0.1', user='admin', passwd='4linux-mori', db='projeto'
	)

print con

# abri sessao
cur = con.cursor()

#insert

try:
	cur.execute(
			"INSERT INTO posts(titulo, conteudo) \
			 VALUES('Meu titulo', 'Meu conteudo')"

		)
	con.commit()

except Exception as e:
	con.rollback()


#update

try:
	cur.execute(
			"UPDATE posts SET titulo='Novo titulo' \
			WHERE ID=2"
		)
	con.commit()

except Exception as e:
	con.roolback()


#SELECT ONE

cur.execute(
		'SELECT * FROM posts WHERE ID=2'
	)

print cur.fetchone()
print '-----------------------------'

cur.execute(
		'SELECT * FROM posts'
	)



print 'Ultimo comando executado '
print cur._last_executed
print '-----------------------------'

for row in cur.fetchall():
	print row


con.close()

