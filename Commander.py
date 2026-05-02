#!/usr/bin/env python3

import time, os

def noTTR(commands):
    try:
        while True:
            for command in commands:
                print(f"> {command}")
                os.system(command)
    except KeyboardInterrupt:
        print("\nStopped")

def TTR(commands):
    try:
        while True:
            for command in commands:
                print(f"> {command}")
                os.system(command)
                time.sleep(0)
    except KeyboardInterrupt:
        print("\nStopped")

def askHowMany():
    try:
        n = int(input("How many commands do you want to repeat? "))
        return n
    except ValueError:
        print("Invalid number")
        askHowMany()

def askTTR():
    try:
        ttr = int(input("Enter Delay in seconds (0 is valid): "))
    except ValueError:
        print("Invalid number")
        return
    
    print("\nRunning... (Ctrl+C to stop)\n")

    if ttr == 0:
        noTTR(commands)
    else:
        TTR(commands)

commands = []

for i in range(askHowMany()):
    command = input(f"Command Nº{i+1}: ")
    commands.append(command)
askTTR()
