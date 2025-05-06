# A interface de rede foi definida como "0.0.0.0", ou seja, qualquer interface ativa no momento.
# Alterar para sua preferência.

import socket, sys

# Função para salvar as logs das vezes que o servidor foi iniciado.
def log_servidor(servidor_iniciado):
		log_servidor = open("servidor.log", "a") # Abrir o arquivo.
		log_servidor.write(servidor_iniciado + "\n") # Escrever o conteúdo armazenado dentro da variável no arquivo aberto.
		log_servidor.close() # Fechar o arquivo.
		print (servidor_iniciado)

# Função para salvar as logs de conexões.
def log_clientes(clientes_conectados):
	log_clientes = open("conexoes.log", "a") # Abrir o arquivo.
	log_clientes.write(clientes_conectados + "\n") # Escrever o conteúdo armazenado dentro da variável no arquivo aberto.
	log_clientes.close() # Fechar o arquivo.
	print (clientes_conectados)


port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket TCP sobre IPv4.
s.bind(("0.0.0.0", port)) # IP e Porta de conexão.
s.listen(1) # Quantas conexões seram aceitas.
log_servidor(f"Aguardando conexão 0.0.0.0 {port}.") # Armazenar as logs de quantos vezes o servidor foi aberto na variável 'servidor_iniciado'.

con, client = s.accept() # Segurar até que alguem se conect no servidor.
log_clientes(f"Conexão {client}") # Armazenar as logs de conexão na variável 'clientes_conectados'.

con.send("Digite a senha: ".encode()) # Solicitar a senha todas as vezes que o usuário se conectar.
senha = con.recv(1024) # Armazenar a senha digitada pelo usuário.

if senha.decode() == "teste\n": # Comprar valores.
	while True:
		# Área do servidor.
		msg = input("> ") # Entrada de dados do servidor.
		msg += "\n"
		if msg == "sair\n": # Encerrar a conexão se o servidor digitar 'sair'.
			print ("Você encerro a conexão.")
			con.send("O servidor encerro a conexão.".encode())
			s.close # Encerrar o socket
			break
		con.send(f"\nServidor: {msg}".encode()) # Enviar os dados do servidor para o cliente.

		# Área do cliente.
		dado_cliente = con.recv(1024).decode() # Receber os dados do cliente.
		print (f"\nCliente: {dado_cliente}")

else:
	print ("O cliente errou a senha e foi desconectado da sessão.")
	con.send("Senha incorreta.".encode())
	s.close() # 'Matar' socket

s.close() # 'Matar' socket
