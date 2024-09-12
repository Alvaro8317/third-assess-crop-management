from azure.cosmos.partition_key import PartitionKey
import azure.cosmos.exceptions as exceptions
from app.domain.entities import Crop
from app.domain.repositories import CropRepository
from app.infrastructure.database.cosmos import CosmosDBSingleton
from app.config.cosmos import settings

partition_key: str = "user_id"


def delete_metadata(obj: dict) -> None:
    obj.pop("_rid")
    obj.pop("_self")
    obj.pop("_etag")
    obj.pop("_attachments")
    obj.pop("_ts")


class CosmosCropRepository(CropRepository):
    def __init__(self):
        self.client = CosmosDBSingleton().database
        container_id = settings.get("container_id")
        try:
            self.container = self.client.create_container(id=container_id,
                                                          partition_key=PartitionKey(path=f'/{partition_key}'))
        except exceptions.CosmosResourceExistsError:
            self.container = self.client.get_container_client(container_id)

    def save(self, crop: Crop) -> Crop:
        self.container.create_item(body=crop.__dict__)
        return crop

    def find_by_id(self, crop_id: str, user_id: int) -> Crop | None:
        try:
            item = self.container.read_item(item=crop_id, partition_key=user_id)
            delete_metadata(item)
            return item
        except exceptions.CosmosResourceNotFoundError:
            return

    def list_all(self, user_id) -> list[Crop]:
        crops = list(self.container.read_all_items(partition_key=user_id))
        return [delete_metadata(item) or item for item in crops]

    def delete(self, crop_id: str, user_id: int) -> bool:
        self.container.delete_item(item=crop_id, partition_key=user_id)
        return True

    def harvest_crop(self, crop, planting_date: str, harvest_date: str) -> Crop:
        crop["planting_date"] = planting_date
        crop["harvest_date"] = harvest_date
        self.container.upsert_item(body=crop)
        return crop
