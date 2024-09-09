# domain/repositories/crop_repository.py
from abc import ABC, abstractmethod
from app.domain.entities import Crop


class CropRepository(ABC):
    @abstractmethod
    def save(self, crop: Crop) -> Crop:
        pass

    @abstractmethod
    def find_by_id(self, crop_id: int) -> Crop:
        pass

    @abstractmethod
    def list_all(self) -> list[Crop]:
        pass

    @abstractmethod
    def delete(self, crop_id: int) -> None:
        pass
