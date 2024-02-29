# Basic Timelapse for Raspberry Pi Camera

This is a simple timelapse script for the Raspberry Pi Camera. It captures images at a set interval and saves them to a folder.

## Usage

```bash
python timelapse.py
```

You can change the interval and the output folder by modifying the script.

You can also run this script in the startup by adding the following line to the `/etc/rc.local` file:

```bash
python /home/pi/timelapse/timelapse.py & /home/pi/timelapse/timelapse.log 2>&1
```

Run `sudo reboot` to restart the Raspberry Pi after adding the line to the `/etc/rc.local` file.

Another way to run the script at startup is to use `cron`. Run `crontab -e` and add the following line:

```bash
@reboot python /home/pi/timelapse/timelapse.py & /home/pi/timelapse/timelapse.log 2>&1
```
