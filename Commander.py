#!/usr/bin/env python3

import time, os
from datetime import datetime


def askHowMany():
    try:
        n = int(input("How many commands do you want to repeat? "))
        return n
    except ValueError:
        print("Invalid number")
        askHowMany()

def askTTR(commands):
    try:
        ttr = int(input("Enter Delay in seconds (0 is valid): "))
    except ValueError:
        print("Invalid number")
        askTTR(commands)
        return
    
    print("\nRunning... (Ctrl+C to stop)\n")

    askWD(commands, ttr)

def askWD(commands, ttr):
    wd = input("Do you want to set a specific working directory? (y/n): ").lower()
    if wd not in ['y', 'n']:
        print("Please answer with 'y' or 'n'")
        return askWD(commands, ttr)
    if wd == 'n':
        return
    elif wd == 'y':
        path = input("Introduce the path: ")
        if os.path.isdir(path):
            os.chdir(path)
            print(f"Working directory set to: {path}")
            pedirHora(commands, ttr)
        else:
            print("Invalid path")
            askWD(commands, ttr)

def pedirHora(commands, ttr):
    answer = input("Do you want to set a specific time to start? (y/n): ").lower()
    if answer not in ['y', 'n']:
        print("Please answer with 'y' or 'n'")
        return pedirHora(commands, ttr)
    if answer == 'n':
        EXE(commands, ttr)
        return
    elif answer == 'y':
        hora = input("Introduce the time (HH:MM:SS): ")
    try:
        time.strptime(hora, "%H:%M:%S")
    except ValueError:
        print("Incorrect format. Use HH:MM:SS")
        return
    waitTime(commands, ttr, hora)

def waitTime(commands, ttr, hora):
    print(f"Waiting until {hora}...")

    while True:
        now = datetime.now().strftime("%H:%M:%S")

        if now == hora:
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

commands = []

for i in range(askHowMany()):
    command = input(f"Command Nº{i+1}: ")
    commands.append(command)
askTTR(commands)
