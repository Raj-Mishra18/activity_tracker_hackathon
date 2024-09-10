# Work Status Agent
Work Status Agent is a Python application designed to monitor user activity, detect timezone changes, and monitor system status including battery level and internet connectivity. The application runs multiple monitoring tasks concurrently using threads.


## Features

#### Activity Monitoring:
* Tracks mouse and keyboard activity and tells if the user is active or inactive.
* Captures screenshots at regular intervals and stores it in the screenshots folder.

#### Timezone Monitoring:
* Monitors changes in the system timezone.
* Logs the detected timezone changes with timestamps.

#### System Status Monitoring:
* Checks for low battery levels and logs warnings.
* Monitors internet connectivity and logs connection/disconnection events.


## Installation
- **Step 1:** Clone the repository from GitHub using the following command:
  ```
  git clone https://github.com/sakshi13042003/Python-Agent-Project.git
  ```
- **Step 2:** Navigate to the project directory

- **Step 3:** Install Dependencies
This project requires several Python libraries. All required libraries are listed in the requirements.txt file. Install them using the following command:
  ```
  pip install -r requirements.txt
  ```
  * The required libraries include:
    * **pynput** (for monitoring mouse and keyboard activity)
    * **Pillow** (for capturing and processing screenshots)
    * **psutil** (for monitoring system resources like battery)
    * **requests** (for checking internet connectivity)

- **Step 3:** Configure the Application
  - No additional configuration is needed, but you can customize settings in the respective script files if required (e.g., screenshot intervals, inactivity thresholds).

## Running the Application
- **Step 1:** To start the application, run the main.py file. This will initiate all monitoring services (activity, timezone, and system status). Use the following command to start the application:
  
  ```
  python main.py
  ```
- **Step 2:** Monitoring Output
  - **Screenshots:** Captured screenshots are saved in the screenshots directory within the project folder.
  - **Logs:** All events, such as timezone changes, internet status, and battery warnings, are logged in the status_log.txt and log.txt files within the project directory.

## Project Structure:
- **main.py:** The main script that starts the monitoring services.
- **activity_tracker.py:** Contains code for tracking user activity and capturing screenshots.
- **timezone_manager.py:** Monitors and logs system timezone changes.
- **status_monitor.py:** Monitors system status such as battery and internet connectivity.
- **requirements.txt:** Lists all required Python libraries.
- **log.txt:** Logs all the timezone changes along with the time when it was done.
- **ststus_log.txt:** Logs all the details regarding internet and battery status.
- **screenshot:** This is folder that stores all the screenshots.

## Customization
- You can customize the following parameters within the code:
  - Screenshot interval (screenshot_interval) in activity_tracker.py.
  - Inactivity threshold (inactive_time_threshold) in activity_tracker.py.
  - Battery and internet check intervals in status_monitor.py.
