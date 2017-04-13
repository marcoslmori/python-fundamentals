# classe.py
# orientado a objeto
# heranca

#definicao de classe

# init eh o construtor

import psycopg2



class Conexao:

	con = None
	cur = None


	def conectar(self, lista):
		self.con = psycopg2.connect(
			"host=%s dbname=%s user=%s password=%s" %
			lista
		)
		self.cur = self.con.cursor()


# permite heranca multipla class Banco(Conexao, Exception)

class Banco(Conexao):

	def __init__(self, lista):
		self.conectar(lista)
	
	def find_one(self, id):
		self.cur.execute("SELECT * FROM  posts WHERE id=%s" % id)
		
		return self.cur.fetchone()



objeto = Banco(('localhost','projeto','postgres','4linux-mori'))


print objeto.cur

print objeto.find_one(1)