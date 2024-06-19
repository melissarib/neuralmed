# Integração com PACS

Este projeto utiliza o Orthanc como servidor PACS/DICOM e Python para facilitar a comunicação e manipulação de imagens médicas.

### Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados em sua máquina:

- [Git](https://git-scm.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop)
- [Python 3.x](https://www.python.org/)

## Instalação

Siga os passos abaixo para configurar o ambiente do projeto:

### 1. Clone o repositório:

```bash
git clone git@github.com:melissarib/neuralmed.git
```

Acesse a branch ```feature/pacs-integration```

### 2. Execute o Docker Desktop
Baixe e instale o Docker Desktop a partir do site oficial. 
Execute-o em segundo plano.

### 3. Baixe a imagem do Orthanc e execute o servidor PACS/DICOM:

```bash
docker pull jodogne/orthanc
```
No arquivo ```/etc/orthanc/orthanc.json```, adicione a AE Title à lista de permissão no servidor DICOM.

Em seguida, execute com o comando

```
docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc
```


### 4. Crie e ative um ambiente virtual Python:
No Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```
### 5. Instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```
## Executando o Projeto
Com o ambiente configurado e as dependências instaladas, você pode executar o projeto. 
Certifique-se de que o servidor Orthanc está em execução e, em seguida, execute seu script Python principal (substitua main.py pelo nome do arquivo que deseja verificar):

```bash
python main.py
```
