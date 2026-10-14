# ==========================================
# Script de Automatización - Laboratorio Cloud Security (AWS S3)
# Estudiante: Sistemas (UNIAJC)
# ==========================================

# 1. Configuración de Credenciales de Prueba
$env:AWS_ACCESS_KEY_ID="test"
$env:AWS_SECRET_ACCESS_KEY="test"
$env:AWS_DEFAULT_REGION="us-east-1"

# 2. Creación del Bucket S3
aws --endpoint-url=http://localhost:4566 s3 mb s3://empresa-datos-sensibles

# 3. Creación y Subida del Archivo Confidencial
Set-Content -Path contrasenas.txt -Value "PASSWORD_DB=Confidencial2026!" -Encoding ascii
aws --endpoint-url=http://localhost:4566 s3 cp contrasenas.txt s3://empresa-datos-sensibles/

# 4. Simulación de la Vulnerabilidad (Ataque: Lectura Pública)
aws --endpoint-url=http://localhost:4566 s3api put-bucket-acl --bucket empresa-datos-sensibles --acl public-read
curl.exe http://localhost:4566/empresa-datos-sensibles/contrasenas.txt

# 5. Remediación (Aplicación de Políticas de Bloqueo de Acceso Público)
aws --endpoint-url=http://localhost:4566 s3api put-bucket-acl --bucket empresa-datos-sensibles --acl private
aws --endpoint-url=http://localhost:4566 s3api put-public-access-block --bucket empresa-datos-sensibles --public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
