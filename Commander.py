#!/usr/bin/env python3

import time, os

# Commander
print("[1] Commander")
print("[2] Slayer Commander (No TTR)")
print("Select option:")
OPTION = input("")

if OPTION == "1":
	# Commander
	print("Enter command:")
	COMMAND = input("")
	print("Enter TTR (Time To Repeat) in seconds:")
	TTR = int(input(""))

	while True:
		os.system(COMMAND)
		time.sleep(TTR)

elif OPTION == "2":

	#Slayer Commander
	print("Enter command:")
	COMMAND = input("")
	print("Are you sure you want to run Slayer Commander? (y/n)")
	CONFIRMATION = input("")

	if CONFIRMATION == "y":
		while True:
			os.system(COMMAND)
	else:
		print("Bye bye")