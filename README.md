# ❤️ AutoCuidado Gym

Projeto-escola de Backend desenvolvido em Python durante minha transição para a área de Tecnologia.

O projeto está sendo construído de forma incremental para aprender, implementar, testar e documentar tecnologias utilizadas no desenvolvimento Backend e, futuramente, em aplicações com Inteligência Artificial.

## 🎯 Objetivo

O AutoCuidado Gym é uma aplicação para registro e acompanhamento de treinos.

Além de ser uma aplicação prática, o projeto funciona como ambiente de aprendizado para desenvolvimento Backend.

## 🛠️ Tecnologias

### ✅ Implementado

- Python
- FastAPI
- API REST
- PostgreSQL
- psycopg2
- Pydantic
- Swagger
- pytest
- Git e GitHub
- Docker
- Docker Compose

### 📌 Funcionalidades implementadas

- Criar exercícios
- Listar exercícios
- Atualizar exercícios
- Excluir exercícios
- Validação de dados com Pydantic
- Testes automatizados da API
- Persistência de dados no PostgreSQL

### 🔄 Próximos passos

- Autenticação com JWT
- GitHub Actions / CI
- Deploy / Cloud
- AWS
- Integração com LLMs
- RAG
- Embeddings
- Banco de dados vetorial

## 🐳 Docker

O projeto utiliza Docker Compose para executar a aplicação em containers separados:

- FastAPI
- PostgreSQL

Os containers se comunicam através da rede criada pelo Docker Compose.

Um volume é utilizado para persistir os dados do PostgreSQL.

## 🧪 Testes

O projeto possui testes automatizados utilizando pytest.

Os testes verificam o funcionamento da API e da integração com o banco de dados.

Atualmente, a suíte de testes possui 6 testes passando.

## 📚 Aprendizado

O desenvolvimento segue o ciclo:

**Aprender → Implementar → Testar → Entender → Aplicar → Versionar**

O objetivo é compreender não apenas o código, mas também como as diferentes tecnologias se conectam em uma aplicação real.

## 🚧 Status

🟡 Projeto em desenvolvimento.

Atualmente, a aplicação possui uma API REST desenvolvida com FastAPI, integrada ao PostgreSQL e executando em containers Docker através do Docker Compose.

O CRUD de exercícios está implementado e testado.

## 💻 Objetivo profissional

Este projeto faz parte da minha transição para Tecnologia e tem como objetivo desenvolver experiência prática em:

- Python
- Desenvolvimento Backend
- APIs
- Bancos de dados
- Testes automatizados
- Docker
- Cloud
- Inteligência Artificial e LLMs