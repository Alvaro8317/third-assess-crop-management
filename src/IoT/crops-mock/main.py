import json
from random import randint
from paho.mqtt import client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
from config.env_vars import ubidot_settings

path_pem = "./roots.pem"


def configure_mqtt():
    client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
    client.username_pw_set(ubidot_settings.get("UBIDOTS_TOKEN"))
    client.tls_set(ca_certs=path_pem)
    client.connect(ubidot_settings.get("BROKER"), 8883)
    return client


def send_data(client):
    payload = json.dumps(
        {
            "temperature": randint(15, 45),
            "humidity": randint(24, 45),
            "soil_moisture": randint(30, 35)
        }
    )
    client.publish(f"/v2.0/devices/{ubidot_settings.get("DEVICE_LABEL")}", payload)
    print("Sent data")


client_udibot = configure_mqtt()
send_data(client_udibot)
client_udibot.disconnect()
