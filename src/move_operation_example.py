from pydicom.dataset import Dataset
from pynetdicom import AE, debug_logger
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelMove
from config import PACS_SERVER

debug_logger()
ae = AE()
ae.add_requested_context(PatientRootQueryRetrieveInformationModelMove)

ds = Dataset()
ds.QueryRetrieveLevel = 'SERIES'

ds.PatientID = 'PCT0014'
ds.StudyInstanceUID = '1.3.6.1.4.1.25403.127722389484638.25552.20200927063148.1'
ds.SeriesInstanceUID = '1.3.6.1.4.1.25403.127722389484638.25552.20200927063148.2'

assoc = ae.associate(PACS_SERVER['IP'], PACS_SERVER['PORT'], ae_title=PACS_SERVER['AET'])

if assoc.is_established:
   
    responses = assoc.send_c_move(ds, 'STORE_SCP', PatientRootQueryRetrieveInformationModelMove)
    for (status, identifier) in responses:
        if status:
            print('⭐ C-MOVE query status: 0x{0:04x}'.format(status.Status))
        else:
            print('🔴 A conexão expirou, foi abortada ou recebeu resposta inválida')
    assoc.release()
else:
    print('🔴 Associação rejeitada, abortada ou nunca conectada durante C-MOVE')