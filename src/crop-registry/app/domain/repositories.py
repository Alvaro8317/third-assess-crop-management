from abc import ABC, abstractmethod
from app.domain.entities import Crop


class CropRepository(ABC):
    @abstractmethod
    def save(self, crop: Crop) -> Crop:
        pass

    @abstractmethod
    def find_by_id(self, crop_id: str, user_id: int) -> Crop:
        pass

    @abstractmethod
    def list_all(self, user_id) -> list[Crop]:
        pass

    @abstractmethod
    def delete(self, crop_id: str, user_id: int) -> bool:
        pass

    def harvest_crop(self, crop, planting_date: str, harvest_date: str) -> Crop:
        pass
