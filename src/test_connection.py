from pynetdicom import AE
from pynetdicom.sop_class import Verification
from src.config import PACS_SERVER

# Inicializa a Entidade de Aplicação
ae = AE()

# Adiciona um contexto de apresentação solicitado
ae.add_requested_context(Verification)

# Associa-se à AE (Application Entity) parceira no IP 127.0.0.1 e porta 4242
assoc = ae.associate(PACS_SERVER['IP'], PACS_SERVER['PORT'])

if assoc.is_established:
    # Usa o serviço C-ECHO para enviar a solicitação
    # retorna o status da resposta como um Dataset do pydicom
    status = assoc.send_c_echo()

    # Verifica o status da solicitação de verificação
    if status:
        # Se a solicitação de verificação foi bem-sucedida, isso será 0x0000
        print('Status da solicitação C-ECHO: 0x{0:04x}'.format(status.Status))
    else:
        print('A conexão expirou, foi abortada ou recebeu uma resposta inválida')

    # Libera a associação
    assoc.release()
else:
    print('Associação rejeitada, abortada ou nunca conectada')
