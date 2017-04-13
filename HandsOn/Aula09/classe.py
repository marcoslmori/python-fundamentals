# classe.py
# orientado a objeto

#definicao de classe

# init eh o construtor

import psycopg2


class Banco:

	con = None

	cur = None


	def __init__(self, host, db, user, passwd):
		self.con = psycopg2.connect(
			"host=%s dbname=%s user=%s password=%s" %
			(host, db, user, passwd)
# acima sao variaveis
		)
		self.cur = self.con.cursor()

	def find_one(self, id):
		self.cur.execute("SELECT * FROM  posts WHERE id=%s" % id)
		
		return self.cur.fetchone()

objeto = Banco('localhost','projeto','postgres','4linux-mori')

print objeto.find_one(1)