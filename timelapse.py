from os import system
from datetime import datetime as dt
from time import sleep
from picamera import PiCamera

# Variables to change
imagesPath = 'home/pi/timelapse/images'
tlminutes = 60 * 24 #set this to the number of minutes you wish to run your timelapse camera
secondsinterval = 60 * 1 #number of seconds delay between each photo taken
fps = 30 #frames per second timelapse video
rotation = 270
resolution = (1280, 720)
initialSleep = 60 * 5 #number of seconds to sleep before starting the timelapse

# No need to change anything below this line

# Check if this script is running on a Raspberry Pi
if os.path.exists(f'{imagesPath}/running.txt'):
    print("Another instance of the script is running. Exiting...")
    exit()

# Sleep for 5 minutes to give user a chance to cancel the script
sleep(initialSleep)

# Create a file to indicate that the script is running
system(f'touch {imagesPath}/running.txt')

# Calculate the number of photos to take
numphotos = int((tlminutes*60)/secondsinterval)
print("Number of photos to take = ", numphotos)

camera = PiCamera()
camera.rotation = rotation
camera.resolution = resolution

for i in range(numphotos):
    camera.capture(f'{imagesPath}/image-{dt.now().strftime("%Y%m%d-%H%M%S")}.jpg')
    sleep(secondsinterval)

print("Done timelapse.")
