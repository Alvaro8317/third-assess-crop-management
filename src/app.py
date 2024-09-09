import grpc
from concurrent import futures
from generated import crop_service_pb2
from generated import crop_service_pb2_grpc
from grpc_reflection.v1alpha import reflection


class CropService(crop_service_pb2_grpc.CropServiceServicer):
    def __init__(self):
        self.crops = {}  # Almacén de datos simple (en memoria)

    def CreateCrop(self, request, context):
        print(type(request))
        crop_id = request.crop.id
        self.crops[crop_id] = request.crop
        return crop_service_pb2.CropResponse(crop=request.crop)

    def GetCrop(self, request, context):
        crop = self.crops.get(request.id)
        if not crop:
            context.set_details("Crop not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return crop_service_pb2.CropResponse()
        return crop_service_pb2.CropResponse(crop=crop)

    def UpdateCrop(self, request, context):
        crop_id = request.crop.id
        self.crops[crop_id] = request.crop
        return crop_service_pb2.CropResponse(crop=request.crop)

    def DeleteCrop(self, request, context):
        if request.id in self.crops:
            del self.crops[request.id]
        return crop_service_pb2.Empty()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    crop_service_pb2_grpc.add_CropServiceServicer_to_server(CropService(), server)
    server.add_insecure_port("[::]:50051")
    # Agregar reflexión al servidor
    SERVICE_NAMES = (
        crop_service_pb2.DESCRIPTOR.services_by_name["CropService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
