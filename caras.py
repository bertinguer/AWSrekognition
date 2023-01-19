import boto3
import sys
import os

# Inicializar el cliente de AWS Rekognition
client = boto3.client("rekognition", region_name="us-east-1", aws_access_key_id="TU_KEY_DE_API_AWS", aws_secret_access_key="TU_PASS_DE_API_AWS")

# Obtener la imagen origen de los parámetros
source_image = sys.argv[1]

# Definir la carpeta de imágenes a comparar
target_folder = "caras/"

# Leer la imagen origen y convertirla en formato binario
with open(source_image, "rb") as image:
    source_bytes = image.read()

# Recorrer todas las imágenes de la carpeta de destino
for target_image in os.listdir(target_folder):
    # Leer la imagen de destino y convertirla en formato binario
    with open(target_folder + target_image, "rb") as image:
        target_bytes = image.read()

# Llamar a la API de AWS Rekognition para comparar las imágenes
    response = client.compare_faces(
        SourceImage={ "Bytes": source_bytes },
        TargetImage={ "Bytes": target_bytes }
    )
    
# Mostrar el tanto por ciento de similitud
    face_matches = response.get("FaceMatches")
    if face_matches:
        similarity = face_matches[0]["Similarity"]
        print("Similitud entre {} y {}: del {:.2f}%".format(source_image, target_image, similarity))
    else:
        print("Similitud entre {} y {}: del 0%".format(source_image, target_image))
