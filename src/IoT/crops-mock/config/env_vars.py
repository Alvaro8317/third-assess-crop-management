import os

from dotenv import load_dotenv

load_dotenv()

ubidot_settings: dict = {
    "UBIDOTS_TOKEN": os.getenv("UBIDOTS_TOKEN"),
    "BROKER": os.getenv("UBIDOTS_URL", "industrial.api.ubidots.com"),
    "DEVICE_LABEL": os.getenv("DEVICE_LABEL", "crop-cundinamarca-01"),
}
