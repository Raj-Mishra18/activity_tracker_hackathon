import time
import datetime
import os
import subprocess
import platform

# Path to log file
log_file = os.path.join(os.getcwd(), "log.txt")

def get_current_timezone():
    """Get the current system timezone."""
    system = platform.system()
    if system == "Windows":
        # Windows command to get timezone
        try:
            result = subprocess.run(['tzutil', '/g'], capture_output=True, text=True)
            timezone = result.stdout.strip()
        except Exception as e:
            print(f"Error getting timezone: {e}")
            timezone = "Unknown"
    elif system == "Linux" or system == "Darwin":
        # Unix-based system command to get timezone
        try:
            result = subprocess.run(['cat', '/etc/timezone'], capture_output=True, text=True)
            timezone = result.stdout.strip()
        except Exception as e:
            print(f"Error getting timezone: {e}")
            timezone = "Unknown"
    else:
        timezone = "Unsupported OS"
    return timezone

def log_timezone_change(previous_timezone, new_timezone):
    """Log the change in timezone."""
    with open(log_file, "a") as log:
        log.write(f"[{datetime.datetime.now()}] Time zone changed from {previous_timezone} to {new_timezone}\n")
    print(f"[{datetime.datetime.now()}] Time zone changed from {previous_timezone} to {new_timezone}")

def monitor_timezone_changes():
    """Monitor and log timezone changes."""
    current_timezone = get_current_timezone()

    while True:
        # Get the new timezone
        new_timezone = get_current_timezone()
        
        # If the timezone has changed, log the new timezone
        if new_timezone != current_timezone:
            log_timezone_change(current_timezone, new_timezone)
            current_timezone = new_timezone

        # Wait for 5 seconds before checking again
        time.sleep(5)

# Example usage (in main.py):
if __name__ == "__main__":
    monitor_timezone_changes()
