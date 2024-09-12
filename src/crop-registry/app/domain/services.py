from app.domain.repositories import CropRepository
from app.domain.entities import Crop
from app.infrastructure.API.crop_model import CropResponseModel


class CropService:
    """
    Service to manage crops.
    """

    def __init__(self, crop_repository: CropRepository):
        """
        Initializes the service with a crop repository.

        :param crop_repository: Repository used to access crop data.
        """
        self.crop_repository = crop_repository

    def get_crop(self, crop_id: str, user_id: int) -> Crop | None:
        """
        Retrieves a crop by its ID.

        :param crop_id: Crop identifier.
        :param user_id: ID of the user requesting the crop.
        :return: The corresponding crop if found, or None if not found.
        """
        crop = self.crop_repository.find_by_id(crop_id, user_id)
        return crop

    def plant_crop(self, crop_data: dict) -> CropResponseModel:
        """
        Registers a new crop applying business rules.

        :param crop_data: Dictionary containing the crop data to be registered.
        :return: Response model with the registered crop data.
        """
        crop = Crop(**crop_data)
        saved_crop = self.crop_repository.save(crop)
        return CropResponseModel(**saved_crop.__dict__)

    def harvest_crop(self, crop_data: dict) -> Crop | bool:
        """
        Marks a crop as harvested.

        :param crop_data: Data of the crop to harvest
        :raises ValueError: If the crop is not found.
        :return: The crop that was harvested.
        """
        crop_id, user_id, harvest_date, planting_date = (
            crop_data["crop_id"], crop_data["user_id"],
            crop_data["harvest_date"], crop_data["planting_date"]
        )
        crop = self.crop_repository.find_by_id(crop_id, user_id)
        if not crop:
            return False
        return self.crop_repository.harvest_crop(crop, planting_date, harvest_date)

    def list_crops(self, user_id: int) -> list[Crop]:
        """
        Lists all crops for the user.

        :param user_id: ID of the user whose crops will be listed.
        :return: List of crops for the user.
        """
        return self.crop_repository.list_all(user_id)

    def delete_crop(self, crop_id: str, user_id: int) -> bool:
        """
        Deletes a crop.

        :param crop_id: Identifier of the crop to be deleted.
        :param user_id: ID of the user requesting the deletion.
        :return: True if the deletion was successful.
        """
        if not self.crop_repository.find_by_id(crop_id, user_id):
            return False
        return self.crop_repository.delete(crop_id, user_id)
