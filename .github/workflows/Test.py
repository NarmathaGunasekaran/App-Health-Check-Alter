import psutil
import requests
import time
import os

# GitHub repo/workflow details
GITHUB_REPO = "your-username/your-repo"
GITHUB_WORKFLOW = "alert.yml"   # Your workflow filename
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Store GitHub PAT in environment variable

# GitHub API endpoint
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_REPO}/actions/workflows/{GITHUB_WORKFLOW}/dispatches"

def trigger_github_action(usage):
    """Trigger GitHub Action workflow with CPU usage"""
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }
    data = {
        "ref": "main",  # branch name
        "inputs": {
            "cpu_usage": str(usage)
        }
    }

    response = requests.post(GITHUB_API_URL, json=data, headers=headers)
    if response.status_code == 204:
        print(f"✅ Alert sent → GitHub Action triggered (CPU: {usage}%)")
    else:
        print(f"❌ Failed to trigger GitHub Action: {response.text}")

def monitor_cpu():
    """Send real-time CPU usage to GitHub Actions"""
    while True:
        usage = psutil.cpu_percent(interval=2)  # check every 2 seconds
        print(f"CPU Usage: {usage}%")
        trigger_github_action(usage)
        time.sleep(5)  # wait 5 sec before next check

if _name_ == "_main_":
    monitor_cpu()
