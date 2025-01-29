from datetime import datetime, timezone
from flask import Flask

app = Flask(__name__)

@app.route("/")
def simple_api():
    # Get the current timezone aware datetime object in UTC format
    current_datetime = datetime.now(timezone.utc)
    # Format the datetime object as string "2025-01-30T09:30:00Z"
    formatted_datetime = current_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")

    response = {
        "email": "lawalmuhammedope@gmail.com",
        "current_datetime": formatted_datetime,
        "github_url": "https://github.com/LmOpe/HNG_BACKEND_STAGE_0"
    }
    return (response, 200)
