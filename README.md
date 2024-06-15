# Projeto de Integração com PACS

1. Clone o repositório:

   ```bash
   git clone git@github.com:melissarib/neuralmed.git
   cd pacs_integration

2. Realize a instalação do Docker Desktop

3. Baixe a imagem do Orthanc como servidor PACS/DICOM

   ```bash
   docker pull jodogne/orthanc
   docker run -p 4242:4242 -p 8042:8042 --rm jodogne/orthanc

4. Realize a instalação do Python 3.x

5. Crie a virtual environment:

   ```bash
   python3 -m venv venv

6. Instale as bibliotecas listadas em `requirements.txt`
   
   ```bash
   pip install -r requirements.txt

7. Execute o projeto 