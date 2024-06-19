# Integração com Prontuário Eletrônico do Paciente (PEP)

Este projeto utilizou o [OpenMRS](https://github.com/openmrs), um sistema de registros médicos de código aberto.

## Instalação

Siga os passos abaixo para configurar o ambiente do projeto:

#### 1. Clone o repositório do OpenMRS

```bash
git clone git@github.com:openmrs/openmrs-distro-referenceapplication.git
```

#### 2. Execute o Docker

```bash
docker compose build
```

```bash
docker compose up
```

#### 3. Faça a autenticação na plataforma
```admin```
```Admin123```

#### 4. Verifique o Swagger do OpenMRS
[Disponível em openmrs/module/webservices/rest/apiDocs](http://localhost/openmrs/module/webservices/rest/apiDocs.htm)

#### 5. Clone o repositório do projeto
```bash
git clone git@github.com:melissarib/neuralmed.git
```

Acesse a branch ```feature/openMRS-integration```

#### 6. Instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

## Executando o projeto
Execute com o comando

```python
fastapi dev main.py
```
Acesse o Swagger da integração em ```localhost:8000/docs``` e teste os endpoints implementados. 
