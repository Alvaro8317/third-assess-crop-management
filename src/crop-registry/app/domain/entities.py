from datetime import date


class Crop:
    def __init__(self, id_crop: int, type_crop: str, variety: str, location: str, size: int, planting_date: date,
                 harvest_date: date, user_id: int):
        self.id = id_crop
        self.type = type_crop
        self.variety = variety
        self.location = location
        self.size = size
        self.planting_date = planting_date
        self.harvest_date = harvest_date
        self.user_id = user_id
