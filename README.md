# CRUD MongoDB
Sistema de estoque em Python com MongoDB, feito como trabalho da disciplina de Banco de Dados (2025/2) com o professor Howard Roatti. Roda no terminal e cobre inserção, consulta, alteração, remoção e relatórios de produtos, fornecedores, funcionários e movimentações de estoque. A modelagem do banco está na pasta `modelagem`.

Feito em grupo com Arthur Pomarolli, Mauro Barros e Pedro Augusto.

## Pré-requisitos
* Linux
* Python 3.10+
* Docker

## Instalação
```bash
git clone https://github.com/thisdev-davi/crud-mongodb.git
cd crud-mongodb
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Banco
O MongoDB roda em um container, sem senha, na porta padrão:

```bash
sudo docker run -d -p 27017:27017 --name mongo-db mongo:latest
```

## Execução
O primeiro comando cria os índices únicos e limpa dados antigos de teste. O segundo abre o sistema.

```bash
python3 src/init_banco.py
python3 main.py
```
