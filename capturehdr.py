# Python script for capturing hdr images
import picamera

def initialize_camera(resolution, exposure_mode):
    """Initializes the python pi camera interface."""
    camera = picamera.PiCamera()
    camera.resolution = resolution
    camera.exposure_mode = exposure_mode
    return camera

def capture_hdr_stack(camera, stops):
    """Captures images with the given EV stops.

    :param stops: EV stops to capture for the HDR stack
    :return: Returns a list of file names of images saved.
    :rtype: list[string]
    """

    file_names = []
    for step in stops:
        # Set filename based on exposure
        filename = 'e%d.jpg' % (step)
        file_names.append(filename)
        # Set camera properties and capture
        camera.exposure_compensation = step
        camera.capture(filename)
    return file_names
