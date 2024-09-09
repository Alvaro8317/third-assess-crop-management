from app.domain.repositories import CropRepository
from app.domain.entities import Crop


class CropService:
    def __init__(self, crop_repository: CropRepository):
        self.crop_repository = crop_repository

    def plant_crop(self, crop_data: dict) -> Crop:
        """Registra un nuevo cultivo, aplicando reglas de negocio."""
        crop = Crop(**crop_data)
        return self.crop_repository.save(crop)

    def harvest_crop(self, crop_id: int) -> Crop:
        """Marca un cultivo como cosechado."""
        crop = self.crop_repository.find_by_id(crop_id)
        if crop is None:
            raise ValueError("Crop not found")
        return crop

    def list_crops(self) -> list[Crop]:
        """Lista todos los cultivos."""
        return self.crop_repository.list_all()
