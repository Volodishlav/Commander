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
    
    askHowManyTimes(commands, ttr)

def askHowManyTimes(commands, ttr):
    
    try:
        times = int(input("How many times do you want to repeat the command? (0 -> infinite) "))
    except ValueError:
        print("Invalid number")
        return askHowManyTimes(commands, ttr)

    if times < 0:
        print("Times cannot be negative")
        return askHowManyTimes(commands, ttr)

    askWD(commands, ttr, times)

def askWD(commands, ttr, times):
    
    wd = input("Do you want to set a specific working directory? (y/n): ").lower()
    if wd not in ['y', 'n']:
        print("Please answer with 'y' or 'n'")
        return askWD(commands, ttr, times)
        
    if wd == 'n':
        askTime(commands, ttr, times)
        
    elif wd == 'y':
        path = input("Introduce the path: ")
        if os.path.isdir(path):
            os.chdir(path)
            print(f"Working directory set to: {path}")
            askTime(commands, ttr, times)
        else:
            print("Invalid path")
            return askWD(commands, ttr, times)

def askTime(commands, ttr, times):
    
    answer = input("Do you want to set a specific time to start? (y/n): ").lower()
    if answer not in ['y', 'n']:
        print("Please answer with 'y' or 'n'")
        return askTime(commands, ttr, times)
        
    if answer == 'n':
        EXE(commands, ttr, times)
        return
        
    elif answer == 'y':
        while True:
                time = input("Introduce the time (HH:MM:SS): ")
                try:
                    time.strptime(time, "%H:%M:%S")
                    break
                except ValueError:
                    print("Incorrect format. Use HH:MM:SS")
        waitTime(commands, ttr, time, times)

def waitTime(commands, ttr, time, times):
    
    print(f"Waiting until {time}...")
    
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now == time:
            EXE(commands, ttr, times)
            break
        time.sleep(1)

def EXE(commands, ttr, times):

    print("\nRunning... (Ctrl+C to stop)\n")

    if times == 0:
        try:
            while True:
                for command in commands:
                    print(f"> {command}")
                    os.system(command)
                    time.sleep(ttr)
        except KeyboardInterrupt:
            print("\nStopped")
    elif times > 0:
        try:
            while times > 0:
                for command in commands:
                    print(f"> {command}")
                    os.system(command)
                    time.sleep(ttr)
                times -= 1
        except KeyboardInterrupt:
            print("\nStopped")
    else:
        raise ValueError("Unexpected error")
        break

def main():

    commands = []

    for i in range(askHowMany()):
        command = input(f"Command Nº{i+1}: ")
        commands.append(command)
    askTTR(commands)

if __name__ == "__main__":
    main()
