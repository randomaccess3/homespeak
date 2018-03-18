# Python3 - Homespeak v0.02
# Query an online Google Home (or Chromecast) device
# usage: python3 homespeak.py <ip> <all|info|bluetooth|networks etc>


# 0.01 - initial commit
# 0.02 - refactor to make adding new get/posts easier and ip formatting validation

# Requirements:
# pip3 install requests (for the get requests)

# https://rithvikvibhu.github.io/GHLocalApi/
#post_header = "content-type: application/json"

def printDivider(div, num ):
	for x in range(0, num):
		print(div, end='')
	print()
	return

import requests, json, sys, argparse, ipaddress

parser = argparse.ArgumentParser()
parser.add_argument("ip", help="ip address of the home device")
parser.add_argument("options", help="options include info, bluetooth, networks, donotdisturb, accessibility, alarms, alarmvolume, wifiscan, appdeviceid, all")
args = parser.parse_args()
#print(args.echo)

# command name = url strings, post/get, print string

command_list = {
    'networks': ["/setup/configured_networks", "get", "Get Configured Networks"],
    'bluetooth': ["/setup/bluetooth/get_bonded", "get", "Get Bluetooth Bonded"],
    'info': ["/setup/eureka_info?params=version,audio,name,build_info,detail,device_info,net,wifi,setup,settings,opt_in,opencast,multizone,proxy,night_mode_params,user_eq,room_equalizer&options=detail", "get", "Get Device Info"],
    'donotdisturb': ["/setup/assistant/notifications", "post", "Get Do Not Disturb"],
    'accessibility': ["/setup/assistant/notifications", "post", "Get Accessibility Settings"],
	'alarms': ["/setup/assistant/alarms", "get", "Get the currently set alarms and timers."],
	'alarmvolume': ["/setup/assistant/alarms/volume", "post", "Get Alarm Volume"],
	'wifiscan': ["/setup/scan_results", "get", "Wifi Scan Results"],
	'appdeviceid': ["/setup/get_app_device_id", "post", "Get App Device ID"],
	}

# validate IP address
try:
    network = ipaddress.IPv4Network(args.ip)
except ValueError:
    print('address/netmask is invalid for IPv4:', args.ip)
    exit(0)

device = "http://"+args.ip+":8008"	

# put options in commands list
if args.options == "all":
	commands = command_list.keys()
elif args.options in command_list.keys():
	commands = [args.options]	
else:
	print("Unknown option: Exiting")
	exit(0)


# for all the commands, run either get or post against the device URL
for c in commands:
	if c in command_list.keys():
		command = command_list[c][0]
		request_method = command_list[c][1]
		print (command_list[c][2])
	else:
		print("Error")
		exit(0)
	
	# sends get/post request and converts json
	if request_method == "get":
		r = requests.get(device + command).json()
	elif request_method == "post":
		r = requests.post(device + command).json()
	else:
		print ("Error")
		exit(0)
				
	# pretties up the json output
	print(json.dumps(r, sort_keys=True, indent=4))
	printDivider("=", 50)