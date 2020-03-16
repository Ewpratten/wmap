
# An empty data frame
empty_frame: dict = {
    "device": -1,
    "timestamp": 0.0,
    "angle": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0
    },
    "accel": {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0
    }
}

# The latest frame of data
latest_frame: dict = empty_frame


def getLatestFrame() -> dict:
    """Get the latest movement frame"""
    if latest_frame["device"] != -1:
        return latest_frame
    else:
        return None

def acceptDeviceLocations(locations:dict):
    pass