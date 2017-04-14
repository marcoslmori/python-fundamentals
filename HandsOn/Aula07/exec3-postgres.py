#exercicio3-postgress.py
#exercicio criar uma lista com varios mais de 2 nomes  e insira todos de uma vez sim 

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# engine = create_engine('sqlite:///banco.db')
engine = create_engine('postgresql://postgres:4linux-mori@localhost:5432/projeto')

Base = declarative_base()

class Usuario(Base):
	__tablename__ = 'usuarios'
	id = Column(Integer, primary_key=True)
	nome = Column(String)

# todos as execucoes so serao executadas ai dentro como se fosse no console


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    #abre uma sessao
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
try:
    lista_nomes=['Joao', 'Jose', 'Alexandra', 'Sandra']
    
    for i in lista_nomes:
        usuario = Usuario(nome=i)
        session.add(usuario)
        session.commit()

    for i in session.query(Usuario).all():
        print i.nome, i.id

except exception as e:
    print e
    session.roolback()


    