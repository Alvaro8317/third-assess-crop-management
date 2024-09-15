import logging
import json
from random import randint
import azure.functions as func
from paho.mqtt import client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
from config.env_vars import ubidot_settings

path_pem = "./roots.pem"
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


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
    logging.info("Sent data")


def manage_mqtt():
    client_udibot = configure_mqtt()
    send_data(client_udibot)
    client_udibot.disconnect()


@app.route(route="hello")
def http_trigger1_test(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    return func.HttpResponse(
        "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
        status_code=200
    )


@app.timer_trigger(schedule="0 */15 * * * *", arg_name="myTimer", run_on_startup=False,
                   use_monitor=False)
def timer_trigger1(my_timer: func.TimerRequest) -> None:
    if my_timer.past_due:
        manage_mqtt()
    logging.info('Python timer trigger function executed.')
