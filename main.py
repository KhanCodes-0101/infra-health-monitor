import requests
import json
from datetime import datetime
import psutil
def log_incident(name, usage, status):
    if status != "NORMAL":
        incident = {
            "resource": name,
            "usage": usage,
            "status": status,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        with open("incidents.json", "a") as file:
            file.write(json.dumps(incident) + "\n")

        print(f"Incident recorded for {name}")
def check_health(name, usage):
    if usage >= 90:
        status = "CRITICAL"
    elif usage >= 80:
        status = "WARNING"
    else:
        status = "NORMAL"

    print(f"{name} Status: {status}")
    log_incident(name, usage, status)

print("== IT INFRASTRUCTURE HEALTH MONITOR ==")
def log_website_incident(url, status, details):
    incident = {
        "website": url,
        "status": status,
        "details": details,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open("incidents.json", "a") as file:
        file.write(json.dumps(incident) + "\n")

    print("Website incident recorded!")

def check_website(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"{url} - Website is UP")

        else:
            print(f"{url} - HTTP Status: {response.status_code}")
            log_website_incident(
                url,
                "WARNING",
                f"HTTP status code: {response.status_code}"
            )

    except requests.RequestException as error:
        print(f"{url} - Website is DOWN or unreachable")

        log_website_incident(
            url,
            "CRITICAL",
            str(error)
        )
def show_incident_report():
    try:
        with open("incidents.json", "r") as file:
            incidents = [
                json.loads(line)
                for line in file
                if line.strip()
            ]

    except FileNotFoundError:
        print("No incident records found.")
        return

    print("\n=== INCIDENT REPORT ===")
    print(f"Total incidents: {len(incidents)}")

    for incident in incidents:
        resource = incident.get(
            "resource",
            incident.get("website", "Unknown")
        )
        status = incident.get("status", "Unknown")
        time = incident.get("time", "Unknown")
        usage = incident.get("usage")
        details = incident.get("details")

        print(f"\nTime: {time}")
        print(f"Resource: {resource}")
        print(f"Status: {status}")

        if usage is not None:
            print(f"Usage: {usage}%")

        if details:
            print(f"Details: {details}")

cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage("C:\\").percent

print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")
print(f"Disk Usage: {disk_usage}%")
check_health("CPU", cpu_usage)
check_health("Memory", memory_usage)
check_health("Disk", disk_usage)
check_website("https://www.google.com")
check_website("https://this-website-does-not-exist-12345.com")
show_incident_report()