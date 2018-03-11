# Python3 - Homespeak
# Query an online Google Home (or Chromecast) device
# usage: python3 homespeak.py <ip> <all|info|bluetooth|networks>

# Requirements:
# pip3 install requests (for the get requests)

#https://rithvikvibhu.github.io/GHLocalApi/

def printDivider(div, num ):
	for x in range(0, num):
		print(div, end='')
	print()
	return

import requests, json, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("ip", help="ip address of the home device")
parser.add_argument("options", help="options include info, bluetooth, networks, all")
args = parser.parse_args()
#print(args.echo)

get_configured_networks = "/setup/configured_networks"
get_bluetooth_bonded = "/setup/bluetooth/get_bonded" #currently connected bluetooth devices
get_device_info = "/setup/eureka_info?params=version,audio,name,build_info,detail,device_info,net,wifi,setup,settings,opt_in,opencast,multizone,proxy,night_mode_params,user_eq,room_equalizer&options=detail"



if args.ip:
	ip = args.ip
if args.options:
	if args.options == "all":
		# add all to array
		commands = ["info", "bluetooth", "networks"]
	elif args.options == "bluetooth":
		commands = ["bluetooth"]
	elif args.options == "networks":
		commands = ["networks"]
	elif args.options == "info":
		commands = ["info"]
	else:
		print("Unknown option: Exiting")
		exit(0)


device = "http://"+ip+":8008"

#post_header = "content-type: application/json"
#post_get_app_device_id = "/setup/get_app_device_id" #unsure what this does

for c in commands:
	if c == "info":
		command = get_device_info
		print("Get Device Info")
	elif c == "bluetooth":
		command = get_bluetooth_bonded
		print("Get Bluetooth Bonded")
	elif c == "networks":
		command = get_configured_networks
		print ("Get Configured Networks")
	else:
		print("Error")
		exit(0)
	
	# sends get request and converts json
	r = requests.get(device + command).json()
	# pretties up the json output
	print(json.dumps(r, sort_keys=True, indent=4))
	printDivider("=", 50)


