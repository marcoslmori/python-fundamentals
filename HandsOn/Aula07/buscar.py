
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///banco.db')
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
    	# usuario = Usuario(nome="Mori")
    	# session.add(usuario)
    	# session.commit()

        # esta buscando o id 1
        usuario= session.query(Usuario).get(1)
        # trazer todos usuario = session.query(Usuarios).all()
        # print session.query(Usuario).filter_by(id=1, nome='Mori').all()
        print usuario.nome

        




except exception as e:
	print e
	session.roolback()


	











