from pydicom import Dataset
from pynetdicom import AE, Association, debug_logger, StoragePresentationContexts
from pynetdicom.sop_class import StudyRootQueryRetrieveInformationModelFind, SecondaryCaptureImageStorage
from config import PACS_SERVER

debug_logger()

ae = AE()
ae.add_requested_context(StudyRootQueryRetrieveInformationModelFind)
ae.add_supported_context(SecondaryCaptureImageStorage)

# Critérios de consulta
ds = Dataset()
ds.QueryRetrieveLevel = 'PATIENT'
ds.PatientName = ''
ds.PatientID = "PCT0014"
ds.StudyInstanceUID = ''

assoc: Association = ae.associate(PACS_SERVER['IP'], PACS_SERVER['PORT'], ae_title=PACS_SERVER['AET'])

if assoc.is_established:
    print(f'✅ Conexão com PACS estabelecida com sucesso!')
    
    # Enviando a requisição C-FIND
    responses = assoc.send_c_find(ds, StudyRootQueryRetrieveInformationModelFind)
    for (status, identifier) in responses:
        if status:
            print('⭐ C-FIND query status: 0x{0:04X}'.format(status.Status))
            
            if identifier is not None:
                print(f'🔍 Dados retornados pelo C-FIND: {identifier}')
                # Verificando se os atributos StudyInstanceUID e SeriesInstanceUID estão presentes
                if hasattr(identifier, 'StudyInstanceUID') and hasattr(identifier, 'SeriesInstanceUID'):
                    print(f'Atributos encontrados: StudyInstanceUID={identifier.StudyInstanceUID}, SeriesInstanceUID={identifier.SeriesInstanceUID}')
                    
                    # Preparando para C-MOVE
                    ds = Dataset()
                    ds.SOPClassUID = SecondaryCaptureImageStorage
                    ds.StudyInstanceUID = identifier.StudyInstanceUID
                    ds.SeriesInstanceUID = identifier.SeriesInstanceUID
                    ds.SOPInstanceUID = identifier.SOPInstanceUID
                    
                    # Realizando o C-MOVE
                    move_assoc = ae.associate(PACS_SERVER['IP'], PACS_SERVER['PORT'], ae_title=PACS_SERVER['AET'])
                    if move_assoc.is_established:
                        try:
                            move_responses = move_assoc.send_c_move(ds, b'\x00\x01')  # b'\x00\x01' é um identificador arbitrário para o destino
                            for (status, _) in move_responses:
                                if status:
                                    print('⭐ C-MOVE query status: 0x{0:04X}'.format(status.Status))
                                else:
                                    print('🔴 A conexão expirou, foi abortada ou recebeu resposta inválida durante C-MOVE')
                        finally:
                            move_assoc.release()
                    else:
                        print('🔴 Associação rejeitada, abortada ou nunca conectada durante C-MOVE')
                else:
                    print(f'🔴 Os atributos StudyInstanceUID e/or SeriesInstanceUID não foram encontrados no resultado da consulta C-FIND. Dados recebidos: {identifier}')
            else:
                print('🔴 Identificador retornado é None.')
        else:
            print('🔴 A conexão expirou, foi abortada ou recebeu resposta inválida durante C-FIND')

    # Liberando a associação principal
    assoc.release()
else:
    print('🔴 Associação rejeitada, abortada ou nunca conectada')
