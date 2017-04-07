#runbanco.py
import psycopg2

con = psycopg2.connect(
	"host=%s dbname=%s user=%s password=%s" % (
     'localhost', 'projeto', 'postgres', '4linux-mori'
     )
)

# trazer uma sessao
cur = con.cursor()

# executa um acao

cur.execute(" \
	INSERT INTO posts(conteudo, titulo) \
	VALUES('A crise no Brasil', 'bla, bla bla')"
	)

con.commit()



