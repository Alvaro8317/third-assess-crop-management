def get_alert_sensor_template(params: dict) -> str:
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sensor Anomaly Alert</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h2 {{
                color: #ff6347;
            }}
            p {{
                margin: 10px 0;
            }}
            .button {{
                display: inline-block;
                padding: 10px 15px;
                background-color: #ff6347;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Sensor Anomaly Detected</h2>
            <p>The sensor <strong>{params.get("sensor")}</strong> has detected an anomaly.</p>
            <p>Received value: <strong>{params.get("value")}</strong></p>
            <p>Please check the system for further details.</p>
            <a href="http://www.google.com" class="button">View Details</a>
        </div>
    </body>
    </html>
    """
