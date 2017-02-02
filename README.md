# README

## SMART Hub Room \ SH Sensor code base 

This code base represents all code related to sensing presence in hub rooms. 

## Dependencies
Installed via pip (python-pip available from Debian repos).

1. python3 (Python 3.x)
1. RPi.GPIO (Already installed on Raspberry Pi)
1. gpiozero (GPIOZero)
1. python3-tk (Tkinter)

Install using the `sudo pip install <package name>` command.

## Setup Guidance
This section outlines steps to access the Pi and run the code.

### SSH 
There is a good guide to finding the RPi IP address with direct ethernet connection [here](http://stackoverflow.com/questions/16040128/hook-up-raspberry-pi-via-ethernet-to-laptop-without-router). 
The guide assumes a Linux environment so you'll need to search for the Windows equivalent if you want to use that. 

The general steps are as follows:

1. Share your connection with the RPi. This is usually achieved in the WiFi settings (IPv4 settings) and changing a drop down to "Share to other computers".
1. Run `ifconfig` to determine your own IP address on the ethernet port. Often 10.x.x.x
1. Connect the ethernet cable between the Pi and Laptop and run `nmap -n -sP <first 3 octets>.255/24` (E.g. `nmap -n -sP 10.42.0.255/24`). This will discover everything on the 10.42.0 network (read up on networkig if you don't understand). 
1. `nmap` may display 2 IP addresses, you want the one that's not a broadcast address, or default gateway address (usually ends in .1)
1. SSH into the Pi using `ssh username@ip_address`, enter the password when prompted and you're in. 

### Running the source
If you're connecting straight into the Pi over SSH you need to share your connection with it, and discover it's IP address. 
Assuming all dependencies are installed and you're in the main app directory, run the following command:

```
sudo python3 main.py
```

## License ####
See LICENSE file.