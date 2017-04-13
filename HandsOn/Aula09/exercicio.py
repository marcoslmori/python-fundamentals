
# aula9 do teacher para verificar

import psycopg2

class Conexao:
    @staticmethod
    def conectar(host, dbname, user, passwd):
        con = psycopg2.connect(
            "host=%s dbname=%s user=%s password=%s" %(
            host, dbname, user, passwd)
        )
        cur = con.cursor()
        return con, cur

class Banco:
    con = None
    cur = None

    def __init__(self, host, dbname, user, passwd):
        self.con, self.cur = Conexao.conectar(host, dbname, user, passwd)

    def find_one(self, id):
        self.cur.execute("SELECT * FROM posts WHERE id=%s" % id)
        return self.cur.fetchone()

class Cadastrar:
    def ingressar(id, titulo):
        self.cur.execute ("INSERT INTO posts (id, titulo) VALUES('%s', '%s')" % (id, titulo))
        try:
            
            if self.cur.rowcount:
                con.commit()
                print '-----------------------------'
                print 'Registro inserido com sucesso!'
                print '-----------------------------'
        except Exception as e:
            cur.roolback()
            print 'falha ao cadastrar'    
        


objeto = Banco('localhost', 'projeto', 'postgres', '4linux-mori')
Cadastrar.ingressar('xico','xica')