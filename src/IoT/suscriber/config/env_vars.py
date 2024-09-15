import os

from dotenv import load_dotenv

load_dotenv()

ubidot_settings: dict = {
    "UBIDOTS_TOKEN": os.getenv("UBIDOTS_TOKEN"),
    "BROKER": os.getenv("UBIDOTS_URL"),
    "DEVICE_LABEL": os.getenv("DEVICE_LABEL"),
}
