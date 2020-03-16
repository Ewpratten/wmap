from webservice.data import empty_frame
from logutil.logging import log

# Device locations
locations: dict = {}


def handleFrame(frame: dict):

    # Device ID Key
    dev_id: str = str(frame["device"])

    # Check if this is the first time we are seeing this device
    if dev_id not in locations.keys():
        log("FrameParser", f"Found new device: {dev_id}")
        locations[dev_id] = {
            "last_frame": frame,
            "pose": {
                "x": 0.0,
                "y": 0.0,
                "z": 0.0
            }
        }
        return

    # Load the last frame
    last_frame: dict = locations[dev_id]["last_frame"]

    # Diffs
    dt: float = frame["timestamp"] - last_frame["timestamp"]
    dax: float = frame["angle"]["x"] - last_frame["angle"]["x"]
    day: float = frame["angle"]["y"] - last_frame["angle"]["y"]
    daz: float = frame["angle"]["z"] - last_frame["angle"]["z"]
    dvx: float = frame["accel"]["x"] - last_frame["accel"]["x"]
    dvy: float = frame["accel"]["y"] - last_frame["accel"]["y"]
    dvz: float = frame["accel"]["z"] - last_frame["accel"]["z"]
    
    # Find dP for each axis
    # dpx:float = 


def getAllLocations() -> dict:
    return locations
