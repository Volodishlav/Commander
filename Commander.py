#!/usr/bin/env python3

import time, os
from datetime import datetime


def askHowMany():
    try:
        n = int(input("How many commands do you want to repeat? "))
        return n
    except ValueError:
        print("Invalid number")
        return askHowMany()

def askTTR(commands):
    try:
        ttr = int(input("Enter Delay in seconds (0 is valid): "))
    except ValueError:
        print("Invalid number")
        return askTTR(commands)
    print("\nRunning... (Ctrl+C to stop)\n")
    askWD(commands, ttr)

def askWD(commands, ttr):
    wd = input("Do you want to set a specific working directory? (y/n): ").lower()
    if wd not in ['y', 'n']:
        print("Please answer with 'y' or 'n'")
        return askWD(commands, ttr)
    if wd == 'n':
        askTime(commands, ttr)
    elif wd == 'y':
        path = input("Introduce the path: ")
        if os.path.isdir(path):
            os.chdir(path)
            print(f"Working directory set to: {path}")
            askTime(commands, ttr)
        else:
            print("Invalid path")
            return askWD(commands, ttr)

def askTime(commands, ttr):
    answer = input("Do you want to set a specific time to start? (y/n): ").lower()
    if answer not in ['y', 'n']:
        print("Please answer with 'y' or 'n'")
        return askTime(commands, ttr)
    if answer == 'n':
        EXE(commands, ttr)
        return
    elif answer == 'y':
        while True:
                time = input("Introduce the time (HH:MM:SS): ")
                try:
                    time.strptime(time, "%H:%M:%S")
                    break
                except ValueError:
                    print("Incorrect format. Use HH:MM:SS")
        waitTime(commands, ttr, time)

def waitTime(commands, ttr, time):
    print(f"Waiting until {time}...")
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now == time:
            EXE(commands, ttr)
            break
        time.sleep(1)  # revisa cada 1 seg

def EXE(commands, ttr):
    try:
        while True:
            for command in commands:
                print(f"> {command}")
                os.system(command)
                time.sleep(ttr)
    except KeyboardInterrupt:
        print("\nStopped")

def main():

    commands = []

    for i in range(askHowMany()):
        command = input(f"Command Nº{i+1}: ")
        commands.append(command)
    askTTR(commands)

if __name__ == "__main__":
    main()
