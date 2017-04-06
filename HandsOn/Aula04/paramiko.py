from paramiko.client import SSHClient
import paramiko

cliente = SSHClient()


client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# client.connect(hostname=host, username=user, password=password)

host = '192.168.202.3'
user = 'noturno'
password = '4linux'

client.connect(hostname=host, username=user, password=password)
stdin, stdout, stderr = client.exec_command("ls - la")

print stdout,read()