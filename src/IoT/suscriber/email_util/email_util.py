import resend
from config.env_vars import resend_api_key
from .template import get_alert_sensor_template

resend.api_key = resend_api_key


def send_email(params: dict, to_email: list[str] | None = None) -> None:
    if to_email is None:
        to_email = ["eduardo831_@hotmail.com"]
    params: resend.Emails.SendParams = {
        "from": "CropsManagerNotifications <onboarding@resend.dev>",
        "to": to_email,
        "subject": "Alert detected in one sensor of the crop",
        "html": get_alert_sensor_template(params),
    }
    result_email = resend.Emails.send(params)
    print(result_email)
