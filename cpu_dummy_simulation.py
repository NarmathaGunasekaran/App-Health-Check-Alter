import os
import requests
import random
import time

# Load Dynatrace secrets
DT_URL = os.environ.get("DT_URL", "").strip()
DT_API_TOKEN = os.environ.get("DT_API_TOKEN", "").strip()

if not DT_URL or not DT_API_TOKEN:
    raise ValueError("DT_URL or DT_API_TOKEN not set!")

endpoint = f"{DT_URL}/api/v2/metrics/ingest"

# Dummy hosts
hosts = ["host-1", "host-2", "host-3", "host-4"]

# Simulation parameters
iterations = 10         # number of times to send metrics
sleep_seconds = 30      # wait time between iterations

for i in range(iterations):
    print(f"--- Iteration {i+1} ---")
    for host in hosts:
        # Random CPU spike between 60-95%
        cpu_value = random.randint(60, 95)
        metric_payload = f"custom.cpu.usage,host={host} {cpu_value}"

        headers = {
            "Authorization": f"Api-Token {DT_API_TOKEN}",
            "Content-Type": "text/plain; charset=utf-8"
        }

        response = requests.post(endpoint, headers=headers, data=metric_payload)

        print(f"Host: {host}, CPU: {cpu_value}%")
        print(f"Status Code: {response.status_code}, Response: {response.text}\n")

    time.sleep(sleep_seconds)
