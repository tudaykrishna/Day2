import time
from datetime import datetime

while True:
    # Get the current date and time
    current_time = datetime.now()
    print("Current Date and Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    
    # Wait for 5 seconds
    time.sleep(5)
