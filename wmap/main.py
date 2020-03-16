from logutil.logging import log
from webservice.data import getLatestFrame, acceptDeviceLocations
from wmap.frameparser import handleFrame, getAllLocations
import time

# Constants
PERIOD: float = 0.02

log("Main", "Program starting")

# Main thread dt
last_time: float = time.clock()

# Data frame dt
last_frame_time: float = 0.0


def run():
    # Read a data frame from the webservice
    frame: dict = getLatestFrame()

    # Skip invalid frames
    if frame["device"] == -1:
        return
    if frame["timestamp"] == last_frame_time:
        return

    # Set the last frame timestamp
    last_frame_time = frame["timestamp"]

    # Handle the frame
    handleFrame(frame)

    # Reflect parsed device data to webservice and logger
    device_locations: dict = getAllLocations()
    acceptDeviceLocations(device_locations)


# Main thread runner
log("Main", "Starting main thread")
log("Main", "Listening for CTRL+C signal")
try:
    while True:

        # Read system time
        now: float = time.clock()

        # Wait for period to pass
        if not (now-last_time) > PERIOD:
            time.sleep(PERIOD/2)
            continue

        # Set the time "checkpoint"
        last_time = now

        # Run the main code
        run()

except KeyboardInterrupt as e:
    print("\r", end="")
    log("Main", "CTRL+C detected")
    log("Main", "Stopping program")
    exit(0)
