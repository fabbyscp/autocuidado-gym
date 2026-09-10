from banco import conectar


conexao = conectar()

print("Conectado ao PostgreSQL!")

conexao.close()