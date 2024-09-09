# third-assess-crop-management

Repository with crop management code - Third assessment, 2024

## Contexto

Somos una startup de innovación enfocado a los cultivos y agricultura. Nuestro enfoque actual es proveer a nuestros usuarios una experiencia agradable para facilitar la gestión de cultivos, conectar a agricultores con compradores y optimizar la cadena de suministro agrícola. La plataforma debe ser robusta, segura y escalable para adaptarse al crecimiento del sector.

### Detalle de **crop management**

- Gestión de Cultivos:

  - Registro detallado de cultivos (tipo, variedad, ubicación, tamaño, fechas de siembra/cosecha).
  - Monitoreo de variables climáticas (temperatura, humedad, precipitación) mediante sensores IoT y APIs externas.
  - Sistema de alertas tempranas para plagas, enfermedades y condiciones climáticas adversas.

### CI Protobuffers

```bash
pip install grpcio-tools
python -m grpc_tools.protoc -I./proto --python_out=./generated --grpc_python_out=./generated ./proto/crop_service.proto
```
