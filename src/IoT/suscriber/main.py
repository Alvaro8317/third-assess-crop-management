import json
import re
import paho.mqtt.client as mqtt
from paho.mqtt.client import Client as PahoClient
from paho.mqtt.client import MQTTMessage
from paho.mqtt.enums import CallbackAPIVersion
from config.env_vars import ubidot_settings
from email_util.email_util import send_email


def on_connect(client, userdata, flags, rc, t):
    print(f"Connected with result code {rc}, userdata {userdata}, flags {flags}, rc {rc}")
    topic_base = f"/v2.0/devices/{ubidot_settings.get('DEVICE_LABEL')}"
    client.subscribe(
        [
            (f"{topic_base}/temperature", 1),
            (f"{topic_base}/humidity", 1),
            (f"{topic_base}/soil_moisture", 1)
        ]
    )


def on_message(client: PahoClient, userdata, msg: MQTTMessage):
    payload_received: dict = json.loads(msg.payload.decode("utf-8"))
    value_got: float = payload_received.get("value")
    pattern = r"crop-cundinamarca-01/(.*)"
    match = re.search(pattern, msg.topic)
    params_email: dict = {
        "value": value_got,
        "sensor": match.group(1)
    }
    if "temperature" in msg.topic and value_got == 30.0:
        send_email(params_email)
    if "humidity" in msg.topic and value_got == 28.0:
        send_email(params_email)
    if "soil_moisture" in msg.topic and value_got == 35.0:
        send_email(params_email)


client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
client.username_pw_set(ubidot_settings.get("UBIDOTS_TOKEN"))
client.tls_set(ca_certs="./roots.pem")
client.on_connect = on_connect
client.on_message = on_message

client.connect(ubidot_settings.get("BROKER"), 8883, 60)

client.loop_forever()
