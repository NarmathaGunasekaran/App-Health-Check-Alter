import os
import requests
import random

# Load and strip Dynatrace URL and API token from environment
DT_URL = os.environ.get("DT_URL", "").strip()
DT_API_TOKEN = os.environ.get("DT_API_TOKEN", "").strip()

if not DT_URL or not DT_API_TOKEN:
    raise ValueError("DT_URL or DT_API_TOKEN not set!")

# Dynatrace Metrics Ingest API endpoint
endpoint = f"{DT_URL}/api/v2/metrics/ingest"

# Simulate CPU usage
cpu_value = random.randint(85, 95)  # dummy CPU spike above threshold
host_name = "dummy-host"

# Correct text format for Dynatrace metrics ingest
metric_payload = f"custom.cpu.usage,host={host_name} {cpu_value}"

headers = {
    "Authorization": f"Api-Token {DT_API_TOKEN}",
    "Content-Type": "text/plain; charset=utf-8"
}

# Send the metric to Dynatrace
response = requests.post(endpoint, headers=headers, data=metric_payload)

# Print results
print(f"Status Code: {response.status_code}")
print("Response:", response.text)
print(f"Sent CPU usage {cpu_value}% for host {host_name}")
