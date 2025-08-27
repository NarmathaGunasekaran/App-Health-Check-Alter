import requests
import os

# Dynatrace environment variables
DT_ENV_URL = os.getenv("DT_ENV_URL")       # Example: https://abc123.live.dynatrace.com
DT_API_TOKEN = os.getenv("DT_API_TOKEN")   # API Token with "events.ingest" permission

url = f"{DT_ENV_URL}/api/v1/events"
headers = {
    "Authorization": f"Api-Token {DT_API_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
  "eventType": "CUSTOM_ALERT",
  "source": "GitHub Action",
  "title": "Dummy CPU Alert",
  "description": "This is a simulated alert sent from GitHub Action"
}

resp = requests.post(url, headers=headers, json=payload)
print("Response:", resp.status_code, resp.text)
