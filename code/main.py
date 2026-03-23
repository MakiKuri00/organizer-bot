from datetime import datetime as dt
import Tasks as T
import serial
import time

HIGHEST_COMMAND_NUM = 7
tasks = T.TaskList()
tasks.load()

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
ser.flush()

def main_title():
    def menu():
        print('Welcome to Organizer Bot!')
        print('[1]: Add a task \n[2]: Delete a task \n[3]: Edit a task \n[4]: Rearrange tasks \n[5]: Save \n[6]: Load \n[7]: Exit')

    menu()

    # todo: Fix alarm
    for i in tasks.task_list:
        i.alarm()

    command = int(input('Enter your option: '))

    while command != 7:
        match command:
            case 1:
                name = input('Enter a new task:')
                dl = input('Enter the deadline for the task (YYY-MM-DD hh:mm:ss): ')
                tasks.add(name, dl)
                tasks.save()
            case 2:
                index = int(input('Which task do you want to remove?'))
                tasks.delete(index)
                tasks.save()
            case 3:
                index = int(input('Choose a task to edit:'))
                new_item = input('Changing to:')
                tasks.edit(index, new_item)
                tasks.save()
            case 4:
                index = int(input('Moving which task?'))
                move_to = int(input('Moving to:'))
                tasks.rearrange(index, move_to)
                tasks.save()
            case 5:
                tasks.save()
            case 6:
                tasks.load()
        menu()
        command = int(input('Enter your option: '))

    print('See you next time!')

while True:
    if ser.in_waiting > 0:
        line = ser.readline()
        print(line)
        while line == "ON":
            main_title()            
        else:
            time.sleep(1000)
