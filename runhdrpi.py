#! /usr/bin/python
# Main script for running the HDR capture-merge sequence
from capturehdr import *
from mergehdr import *
from time import sleep
from datetime import datetime
from subprocess import call

if __name__=="__main__":
    # Options for timelapse
    number_of_images = 10 #2160
    delay = 10
    basename = 'image'
    datestring = datetime.now().__format__('%Y-%m-%d_%I%p')
    timelapse_video_name = '%s.mp4' % (datestring)

    # Options for capture
    ev_stops = [-20, 0, 20]
    exposure_mode = 'auto'
    # resolution = (800, 600)
    # resolution = "720p"
    resolution = (2592, 1944)
    # avconv -r 25 -i img_%04d.jpg -vf "scale=1280:960,crop=1280:720:0:87" -vcodec libx264 -crf 20 -g 15 tl.mp4

    # Options for merging
    # nothing yet
    # Options for ffmpeg
    frames_per_second = 10
    # video_filters = "scale=1280:960,crop=1280:720:0:87"
    video_filters = "scale=1280:960"

    # Log file
    f = open('hdrpi.log', 'a')
    f.write('Starting HDR sequence.\n')
    f.write('Current Time: ' + datetime.now().isoformat())

    camera = initialize_camera(resolution, exposure_mode)
    f.write('Initialized Camera.\n')

    # Capture our images
    for image_number in range(1, number_of_images + 1):
        file_names = capture_hdr_stack(camera, ev_stops)
        f.write('Captured HDR Stack.\n')

        # Merge them into an HDR image
        hdr_image_name = '%s_%04d.jpg' % (basename, image_number)
        merge_hdr_stack(file_names, hdr_image_name)

        f.write('Merged HDR Stack.\n')
        sleep(delay)

    # Create the time lapse
    call([
        "avconv",
        "-r", str(frames_per_second),
        "-i", "{basename}_%04d.jpg".format(basename=basename),
        "-vf", video_filters,
        "-vcodec", "libx264", "-crf",  "20", "-g", "15",
        timelapse_video_name
    ])

    f.write('Wrote video\n.')
    f.write('Current Time: ' + datetime.now().isoformat())
