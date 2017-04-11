#step2
import psycopg2
import os

flag = True

host = 'localhost'
dbname = 'projeto'
user = 'postgres'
password = '4linux-mori'

con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (host, dbname, user, password))
cur = con.cursor()

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

        query = "SELECT * FROM users WHERE usuario='%s' AND pass='%s'" % (user, pswd)
        cur.execute(query)

        usuario = cur.fetchone()

        if usuario:
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
        
        cadastrar = "INSERT INTO users (usuario, pass) VALUES('%s', '%s')" % (user, pswd)
        
        try:

            cur.execute(cadastrar)
            if cur.rowcount:
                con.commit()
                print '-----------------------------'
                print 'Registro inserido com sucesso!'
                print '-----------------------------'
        except Exception as e:
            cur.roolback()
            print 'falha ao cadastrar'    
        
    elif option == 3:
        os.system("clear")
        print 'Opcao 3 selecionada'
        print 'lista usuarios'
        user = raw_input('Usuario: ')
        mostrar = "SELECT * FROM users WHERE usuario LIKE '%%%s%%'" % user;
        cur.execute(mostrar)
        usuario = cur.fetchone()
        if usuario: 
            print '==================='
            print 'Usuario: %s\nSenha: %s' %(usuario[1], usuario[2])
            print '==================='

    elif option == 4:
        os.system("clear")
        print 'Volte sempre'
        exit()