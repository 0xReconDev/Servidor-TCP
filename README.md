# 🧪 Servidor TCP com Autenticação e Log – Python

Este é um servidor TCP simples desenvolvido em **Python**, que implementa:
- Autenticação por senha
- Registro de logs (servidor e clientes)
- Comunicação bidirecional entre servidor e cliente

✅ Ideal para estudo de **sockets**, **conexões TCP**, **entrada e saída de dados** e **segurança básica**.

---

## ⚠️ Aviso Legal

> ❗ **Uso apenas para fins educacionais!**
>
> Não use este script para conexões maliciosas ou sem permissão. Estudar redes é essencial, mas deve ser feito de forma ética.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Bibliotecas padrão:
  - `socket`
  - `sys`

---

## 📄 Funcionalidades

🔐 **Autenticação por senha**  
📓 **Registro em log de inicialização do servidor** (`servidor.log`)  
📓 **Registro em log de conexões de clientes** (`conexoes.log`)  
💬 **Comunicação interativa entre servidor e cliente**  
🔚 **Finalização da sessão com comando `sair`**

---

## ▶️ Como Executar

### 1. Inicie o servidor

```bash
python3 servidor.py <PORTA>
```
### 2. Conectar no Servidor
- Para realizar a conexão, pode-se utilizar ferramentas como: nc, telnet, socat e etc.
```bash
nc -vn 0.0.0.0 <PORTA>
```

## ⚠️ Aviso Importante
- A interface de rede no script foi definida como '0.0.0.0', ou seja, qualquer interface.
```bash
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", port))
```
- Altere para interface que você deseja, ou crie uma entrada de dados para escolher essa interface sem ter que entrar no script o tempo todo.

- A senha de autênticação foi definida apenas para teste. Pode ser removida ou alterada.
```bash
con.send("Digite a senha: ".encode())
senha = con.recv(1024)
if senha.decode() == "teste\n":
```
