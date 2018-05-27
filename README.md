# homespeak
Script for querying Google home devices

Python version: Python3
Library requirements: requests (pip3 install requests)

Usage:
python3 homespeak.py <ip> <all|info|bluetooth|networks etc>

Expected usage:
python3 homespeak.py <ip> info | grep "cloud_device_id"
python3 homespeak.py <ip> bluetooth

------------------------------------------------------------------------------------------------

To Find Home devices on your network run
nmap -p 8008,8009,9000,10001 192.168.0.1-255 --open
