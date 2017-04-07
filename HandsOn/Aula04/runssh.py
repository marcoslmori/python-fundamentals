from paramiko.client import SSHClient
import paramiko
import os

client = SSHClient()


client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# client.connect(hostname=host, username=user, password=password)
#ip da maquina fisica - para saber veja ifconfig
host = '192.168.202.3'
user = 'noturno'
password = '4linux'

#executa no servidor conectado
client.connect(hostname=host, username=user, password=password)

stdin, stdout, stderr = client.exec_command("la -la")
print stdout.read()

# Controle de erro
if stderr.channel.recv_exit_status() != 0:
	print stderr.channel.recv_exit_status()
	print stderr.read()
else:
	print stdout.read()

stdin, stdout, stderr = client.exec_command("/sbin/ifconfig")
print stdout.read()

# executa local 
print os.popen("ls -la").read()

# status da execucao do comando 
# $? --> fica o status do sucesso do comando

