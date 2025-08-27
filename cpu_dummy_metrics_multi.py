import os
import requests
import random

# Load Dynatrace secrets
DT_URL = os.environ.get("DT_URL", "").strip()
DT_API_TOKEN = os.environ.get("DT_API_TOKEN", "").strip()

if not DT_URL or not DT_API_TOKEN:
    raise ValueError("DT_URL or DT_API_TOKEN not set!")

endpoint = f"{DT_URL}/api/v2/metrics/ingest"

# List of dummy hosts
hosts = ["host-1", "host-2", "host-3", "host-4"]

# Send random CPU spikes for each host
for host in hosts:
    cpu_value = random.randint(85, 95)  # spike above threshold
    metric_payload = f"custom.cpu.usage,host={host} {cpu_value}"

    headers = {
        "Authorization": f"Api-Token {DT_API_TOKEN}",
        "Content-Type": "text/plain; charset=utf-8"
    }

    response = requests.post(endpoint, headers=headers, data=metric_payload)

    print(f"Host: {host}, CPU: {cpu_value}%")
    print(f"Status Code: {response.status_code}, Response: {response.text}\n")
