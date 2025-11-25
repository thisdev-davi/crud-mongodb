# Projeto CRUD com MongoDB - Execução no Linux
Este projeto implementa um CRUD (Create, Read, Update, Delete) em **Python**, com integração ao **noSQL MongoDB**.  
O ambiente de execução proposto é **Linux**.
<br>

## Pré-requisitos 🐧
Antes de iniciar, garanta que o seu ambiente Linux possua:
<br>

- **python 3.10+**
- **pip** (gerenciador de pacotes do Python)
- **docker**

## Criando o Ambiente Virtual (venv)
Antes de tudo, clone o projeto do GitHub 🐱:
```bash
git clone https://github.com/thisdev-davi/crud-mongodb.git
```

Para isolar as dependências do projeto:

1. No diretório do projeto crie o ambiente virtual:
   ```bash
   python3 -m venv venv
   ```

2. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```

3. Com o ambiente ativo, instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```
<br>

## Configuração da Conexão com o Banco 🐳
Para executar o projeto, é necessário que o Oracle Database esteja rodando.
Você pode usar uma instalação local ou, de forma mais prática, utilizar o Docker.

> Caso não possua o Oracle instalado, utilize o container oficial Oracle XE
<br>

1. Baixe a imagem oficial do MongoDB:
   ```bash
   sudo docker pull mongo:latest
   ```
2. Crie e inicie o container (sem senha para ambiente de desenvolvimento):
   ```bash
   sudo docker run -d -p 27017:27017 --name mongo-db mongo:latest
   ```
3. Confirme que o container está rodando:
   ```bash
   sudo docker ps
   ```
<br>

## Execução do Projeto
Após ter feito os passos acima, rode esses comandos dentro da pasta do projeto clonado:

1. Crie as tabelas no banco. Diferente do SQL, o Mongo cria coleções automaticamente. Porém, para criar os Índices Únic (Constraints) e limpar dados antigos de teste, execute:
   ```bash
   python3 src/init_banco.py
   ```

2. Execute o CRUD:
   ```bash
   python3 main.py
   ```