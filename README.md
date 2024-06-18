# Integração com PEP (Banco de Dados)

Este projeto faz uso da biblioteca psycopg2-binary, que fornece uma interface para a linguagem de programação Python se comunicar com o banco de dados PostgreSQL. Com ela é possível que consultas SQL e comandos do banco de dados PostgreSQL sejam executadas normalmente, além de permitir a recuperação e manipulação dos resultados das consultas.

Também é possível se conectar a um banco de dados PostgreSQL que esteja hospedado em qualquer lugar, incluindo na nuvem, desde que você tenha as credenciais de acesso e o endereço correto do servidor.

#### Instalação
Para instalar o psycopg2-binary, você pode usar o gerenciador de pacotes pip:

```bash
pip install psycopg2-binary
```

Para utilizar o script, basta alterar as credenciais a partir da linha 3, em "detalhes da conexão".

```
dbname      # Nome do banco de dados
user        # Usuário do banco de dados
password    # Senha do banco de dados
host =      # Endereço do servidor
port =      # Porta do PostgreSQL
```

Execute com o comando

```bash
python postgresql.py
```