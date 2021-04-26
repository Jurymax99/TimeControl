from datetime import datetime
import time
import os
import csv

def help():
    print("Enter s to start counting your worktime")
    print("Once started, enter p to pause, r to resume or s to stop the clock")
    print("Enter q to quit")

def invalid():
    print("Invalid input")

csv_columns = ['Day', 'Hour', 'WorkTime', 'Concept']
csv_file = "data.csv"

def runClock():
    print("Clock started")
    finished = False
    startTime = datetime.now()
    initDay = startTime.strftime("%d/%m/%Y")
    initHour = startTime.strftime("%H:%M:%S")
    while(not finished):
        entrada = input()
        if entrada == "s":
            concept = input("Enter work done: ")
            finishTime = datetime.now()
            worktime = finishTime - startTime
            print("The " + initDay + " at " + initHour + " worked " + str(worktime) + " in " + concept)
            try:
                with open(csv_file, 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=csv_columns)
                    writer.writerow({'Day': initDay, 'Hour': initHour, 'WorkTime': str(worktime), 'Concept': concept})
            except IOError:
                print("I/O error")
            finished = True
        # elif entrada == "p":
            # TODO: Pause function
        elif entrada == "h":
            help()
        else:
            invalid()


def init():
    if not os.path.exists(csv_file) or os.stat(csv_file).st_size == 0:
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=csv_columns)
                writer.writeheader()
                print("Created file data.csv with info")
        except IOError:
            print("I/O error")

if __name__ == "__main__":
    init()
    print("Welcome, enter a valid command (h for more info)")
    finished = False
    while(not finished):
        entrada = input()
        if entrada == "h":
            help()
        elif entrada == "s":
            runClock()
        elif entrada == "q":
            finished = True
            print("Quitting ...")
        else:
            invalid()
            