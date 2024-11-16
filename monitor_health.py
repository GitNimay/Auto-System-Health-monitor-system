import psutil
import time
import logging
from twilio.rest import Client
import platform

# Set up logging (using raw string literal for Windows compatibility)
logging.basicConfig(
    filename=r"system_health.log",  # Use forward slashes or raw string literals for Windows
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Twilio configuration - make sure to replace these with your own values
TWILIO_ACCOUNT_SID = 'YOUR_SID'
TWILIO_AUTH_TOKEN = 'YOUR_TOKEN'
FROM_PHONE = 'TWILIO_NUMBER'
TO_PHONE = 'YOUR_PHONE_NUMBER'


# Function to send SMS alert
def send_sms_alert(message):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=FROM_PHONE,
            to=TO_PHONE
        )
        logging.info(f"SMS sent: {message.sid}")
        print(f"SMS sent: {message.sid}")  # Output SMS sent status to terminal
    except Exception as e:
        logging.error(f"Error sending SMS: {e}")
        print(f"Error sending SMS: {e}")  # Output error to terminal


# Function to monitor system health
def monitor_system_health():
    while True:
        # Get CPU, Memory, and Disk Usage
        cpu_usage = psutil.cpu_percent(interval=1)  # 1 second interval to get accurate reading
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        # Prepare the log message
        message = (
            f"CPU Usage: {cpu_usage}% | "
            f"Memory Usage: {memory.percent}% | "
            f"Disk Usage: {disk.percent}%"
        )

        # Log the system health
        logging.info(message)
        print(f"System Health: {message}")  # Output system health status to terminal

        # Check for threshold violations and send SMS alert if necessary
        if cpu_usage > 45:
            alert_message = f"High CPU usage detected: {cpu_usage}%"
            logging.warning(alert_message)
            print(f"Warning: {alert_message}")  # Output to terminal
            send_sms_alert(alert_message)

        if memory.percent > 45:
            alert_message = f"High Memory usage detected: {memory.percent}%"
            logging.warning(alert_message)
            print(f"Warning: {alert_message}")  # Output to terminal
            send_sms_alert(alert_message)

        if disk.percent > 45:
            alert_message = f"High Disk usage detected: {disk.percent}%"
            logging.warning(alert_message)
            print(f"Warning: {alert_message}")  # Output to terminal
            send_sms_alert(alert_message)

        # Sleep for a specified time before next check (e.g., 1 minute)
        time.sleep(15)  # Change the sleep interval as needed


# Run the system health monitor
if __name__ == "__main__":
    if platform.system() == "Windows":
        logging.info("System health monitoring started on Windows.")
        print("System health monitoring started on Windows.")  # Output to terminal
    else:
        logging.info(f"System health monitoring started on {platform.system()}.")
        print(f"System health monitoring started on {platform.system()}.")  # Output to terminal

    monitor_system_health()
