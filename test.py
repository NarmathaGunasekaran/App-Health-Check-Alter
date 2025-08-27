import os
import requests
import random

DT_URL = os.environ.get("DT_URL")
DT_API_TOKEN = os.environ.get("DT_API_TOKEN")

if not DT_URL or not DT_API_TOKEN:
    raise ValueError("DT_URL or DT_API_TOKEN not set!")

# Dynatrace Metrics Ingest API
endpoint = f"{DT_URL}/api/v2/metrics/ingest"

# Generate dummy CPU usage above threshold
cpu_value = random.randint(85, 95)  # assuming threshold is 80%
host_name = "dummy-host"

# Metric payload
metric_payload = f"builtin:host.cpu.usage,host={host_name} value={cpu_value}"

# Headers
headers = {
    "Authorization": f"Api-Token {DT_API_TOKEN}",
    "Content-Type": "text/plain; charset=utf-8"
}

response = requests.post(endpoint, headers=headers, data=metric_payload)

print(f"Status Code: {response.status_code}")
print("Response:", response.text)
print(f"Sent CPU usage {cpu_value}% for host {host_name}")
