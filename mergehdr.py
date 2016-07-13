# A script for merging the HDR stack using enblend / enfuse
from subprocess import call
from datetime import datetime

def merge_hdr_stack(file_names=None, image_name=None):
    """Merge given list of image file names into a HDR image.

    :param file_names: List of files names to combine to a HDR image
    :type file_names: list[str]
    :param image_name: Name of the merged HDR image
    :type image_name: str
    """
    if image_name is None:
        now = datetime.now()

        # Create a formated date for the file name
        date = now.__format__('%Y-%m-%d')
        seconds_since_midnight = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        minutes = int(seconds_since_midnight/60)
        image_name = '%sT%04d.jpg' % (date, minutes)
    
    outfile = '--output=%s' % (image_name)

    call(["enfuse", outfile] + file_names)
    print("wrote file %s" % (image_name))
    return True
