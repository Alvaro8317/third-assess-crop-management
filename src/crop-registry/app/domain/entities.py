from datetime import date
from datetime import datetime
import uuid


class Crop:
    def __init__(self, crop_type: str, variety: str, location: str, size: int, planting_date: date,
                 harvest_date: date, user_id: int):
        self.crop_type = crop_type
        self.harvest_date = harvest_date
        self.id = str(uuid.uuid4())
        self.insert_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.location = location
        self.planting_date = planting_date
        self.size = size
        self.user_id = user_id
        self.variety = variety
