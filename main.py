from src.dicom_operations import find_dicom_images, move_dicom_images

def main():
    patient_id = 'STS_007'
    destination_ae = 'DEST_AE'
    
    print("Encontrar imagens DICOM para:", patient_id)
    find_dicom_images(patient_id)
    
    print("Mover imagens DICOM para:", destination_ae)
    move_dicom_images(patient_id, destination_ae)

if __name__ == "__main__":
    main()