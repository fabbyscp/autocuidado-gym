# AutoCuidado Gym API

API REST para gerenciamento de exercícios físicos, desenvolvida com Python e FastAPI. O projeto utiliza PostgreSQL para persistência de dados, autenticação JWT, testes automatizados e Docker.

A aplicação foi desenvolvida como projeto prático de Backend, contemplando desenvolvimento de APIs, integração com banco de dados, autenticação, testes e deploy em ambiente de produção.

## Demonstração

- **API em produção:** https://autocuidado-gym.onrender.com
- **Documentação interativa (Swagger):** https://autocuidado-gym.onrender.com/docs

## Tecnologias

- Python 3.12
- FastAPI
- PostgreSQL
- psycopg2
- Pydantic
- JWT (PyJWT)
- Bcrypt
- Docker e Docker Compose
- Pytest
- Git e GitHub
- GitHub Actions
- Render
- Neon

## Funcionalidades

### Autenticação
- Cadastro de usuários
- Armazenamento de senhas com hash bcrypt
- Login com autenticação JWT
- Proteção das rotas de exercícios por token

### Gerenciamento de exercícios
- Criar exercícios
- Listar exercícios
- Atualizar exercícios
- Excluir exercícios
- Validação de dados com Pydantic

## Endpoints

| Método | Rota | Descrição | Autenticação |
|---|---|---|---|
| POST | `/usuarios` | Cadastrar usuário | Não |
| POST | `/login` | Realizar login | Não |
| GET | `/exercicios` | Listar exercícios | Sim |
| POST | `/exercicios` | Criar exercício | Sim |
| PUT | `/exercicios/{id}` | Atualizar exercício | Sim |
| DELETE | `/exercicios/{id}` | Excluir exercício | Sim |

## Banco de dados

O projeto utiliza PostgreSQL para armazenar usuários e exercícios.

A conexão é configurada por variáveis de ambiente, permitindo utilizar diferentes bancos de dados nos ambientes local e de produção.

## Testes automatizados

Os testes são desenvolvidos com Pytest e verificam o funcionamento da API e suas operações.

- 6 testes automatizados passando.
- Integração contínua configurada com GitHub Actions.

## Docker

A aplicação utiliza Docker Compose para executar a API e o PostgreSQL em containers separados.

## Executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/fabbyscp/autocuidado-gym.git
cd autocuidado-gym
```

### 2. Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as configurações do banco de dados e a chave JWT.

Não compartilhe nem versione esse arquivo.

### 3. Iniciar os containers

```bash
docker compose up -d --build
```

### 4. Acessar a documentação

Com a aplicação em execução:

http://localhost:8000/docs

### 5. Executar os testes

```bash
pytest
```

## Deploy

A API está publicada no Render e utiliza PostgreSQL hospedado no Neon.

## Objetivo do projeto

O AutoCuidado Gym faz parte da minha trajetória de desenvolvimento na área de Tecnologia, com foco em Python, Backend e construção de aplicações.

O projeto permitiu praticar conceitos importantes de desenvolvimento de software, desde a implementação de endpoints até autenticação, persistência de dados, testes automatizados e publicação em produção.