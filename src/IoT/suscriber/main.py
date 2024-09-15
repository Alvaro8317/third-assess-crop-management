import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
from config.env_vars import ubidot_settings


def on_connect(client, userdata, flags, rc, t):
    print(f"Connected with result code {rc}, userdata {userdata}, flags {flags}, rc {rc}")
    topic = f"/v2.0/devices/{ubidot_settings.get("DEVICE_LABEL")}/temperature"
    client.subscribe(topic)


def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")


client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2)
client.username_pw_set(ubidot_settings.get("UBIDOTS_TOKEN"))
client.tls_set(ca_certs="./roots.pem")
client.on_connect = on_connect
client.on_message = on_message

client.connect(ubidot_settings.get("BROKER"), 8883, 60)

client.loop_forever()
