import psutil
import requests
import time
import datetime
import os

# Path to log file
log_file = os.path.join(os.getcwd(), "status_log.txt")

def log_status_change(status):
    with open(log_file, "a") as log:
        log.write(f"[{datetime.datetime.now()}] {status}\n")
    print(f"{status}")

def check_battery_status():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        plugged_in = battery.power_plugged
        if percent < 20 and not plugged_in:
            log_status_change(f"Low battery detected: {percent}% remaining and not plugged in.")
        elif percent < 20 and plugged_in:
            log_status_change(f"Low battery detected: {percent}% remaining but plugged in.")
    else:
        log_status_change("Battery status not available.")

def check_internet_connection(last_status):
    try:
        # Check for an active internet connection by making a request to a reliable site
        requests.get("https://www.google.com", timeout=5)
        current_status = "connected"
    except (requests.ConnectionError, requests.Timeout):
        current_status = "disconnected"
    
    # Log only if the status has changed
    if current_status != last_status:
        log_status_change(f"Internet is {current_status}.")
    
    return current_status

def monitor_system_status():
    last_internet_status = None
    battery_check_interval = 60  
    internet_check_interval = 1  
    last_battery_check_time = time.time()

    while True:
        current_time = time.time()

        # Check internet status every 5 seconds
        last_internet_status = check_internet_connection(last_internet_status)
        
        # Check battery status every 60 seconds
        if current_time - last_battery_check_time >= battery_check_interval:
            check_battery_status()
            last_battery_check_time = current_time

        # Sleep for the internet check interval
        time.sleep(internet_check_interval)

# Example usage (in main.py):
if __name__ == "__main__":
    monitor_system_status()
