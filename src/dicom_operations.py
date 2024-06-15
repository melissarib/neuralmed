from pydicom import Dataset
from pynetdicom import AE, Association, debug_logger
from pynetdicom.sop_class import StudyRootQueryRetrieveInformationModelFind
from config import PACS_SERVER

debug_logger()

ae = AE()
ae.add_requested_context(StudyRootQueryRetrieveInformationModelFind)

# Critérios de consulta
ds = Dataset()
ds.QueryRetrieveLevel = 'STUDY'
ds.PatientID = "STS_007"

assoc: Association = ae.associate(PACS_SERVER['IP'], PACS_SERVER['PORT'], ae_title="ORTHANC")

if assoc.is_established:
    print(f'✅ Conexão com PACS estabelecida com sucesso!')
    
    # Enviando a requisição C-FIND
    responses = assoc.send_c_find(ds, StudyRootQueryRetrieveInformationModelFind)
    for (status, identifier) in responses:
        if status:
            print('⭐ C-FIND query status: 0x{0:04X}'.format(status.Status))
        else:
            print('🔴 A conexão expirou, foi abortada ou recebeu resposta inválida')

    # Liberando a associação
    assoc.release()
else:
    print('🔴 Associação rejeitada, abortada ou nunca conectada')
