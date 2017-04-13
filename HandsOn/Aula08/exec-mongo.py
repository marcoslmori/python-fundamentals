# exec-mongo.py

from pymongo import MongoClient
import os

flag = True

# quando instancia ja executa
client = MongoClient('127.0.0.1')
db = client['devops']


session = False

while flag:
    banner = '''Menu:
1) Logar
2) Cadastrar usuario
3) Lista usuario
4) Sair
Selecione a opcao: '''

    option = int(raw_input(banner))
    
    if option == 1:
        os.system("clear")
        user = raw_input('Username: ')
        pswd = raw_input('Password: ')

        # query = "SELECT * FROM users WHERE usuario='%s' AND pass='%s'" % (user, pswd)
        query =  db.fila.find({"nome" : user, "senha" : pswd })

        # cur.execute(query)

        # usuario = cur.fetchone()


        if query.count() != 0:
            session=True
            print 'Login com sucesso'
        else:
            print 'Username ou password invalidos'
    
    elif option == 2:
        os.system("clear")
        if not session:
            print 'Usuario nao logado'
            continue

        print 'Opcao 2 selecionada'
        print 'Digite as informacoes: '
        user = raw_input('Username: ')
        pswd = raw_input('Password: ')
        
        # cadastrar = "INSERT INTO users (usuario, pass) VALUES('%s', '%s')" % (user, pswd)
        cadastrar = db.fila.insert({ "nome": user, "senha": pswd})
		# cadastrar = db.fila.insert({"nome": user, "senha": pswd})

        
    elif option == 3:
        os.system("clear")
        print 'Opcao 3 selecionada'
        print 'lista usuarios'
        user = raw_input('Usuario: ')
        # mostrar = "SELECT * FROM users WHERE usuario LIKE '%%%s%%'" % user;
        mostrar = db.fila.find({"nome": user})

        # cur.execute(mostrar)
        # usuario = cur.fetchone()

        ## checar nao funcionou

        if mostrar.count() != 0: 
            print '==================='
            print 'Usuario: %s\nSenha: %s' %(mostrar[0]['nome'], mostrar[0]['senha'])
            print '==================='


            # print '===================='
            # print 'Usuario: %s\nSenha: %s' % (result[0]['usuario'], result[0]['senha'])
            # print '===================='




    elif option == 4:
        os.system("clear")
        print 'Volte sempre'
        exit()