import os
import json
import datetime
import Tasks

HIGHEST_COMMAND_NUM = 4
print('Welcome to Organizer Bot!')

command = int(input('[1]: Add a task \n[2]: Delete a task \n[3]: Edit a task \n[4]: Rearrange tasks \n[5]: Exit'))
tasks = Tasks.TaskList()
while command != 5:
    match command:
        case 1:
            item = input('Enter a new task:')
            tasks.add(item)
        case 2:
            index = int(input('Which task do you want to remove?'))
            tasks.delete(index)
        case 3:
            index = int(input('Choose a task to edit:'))
            new_item = input('Changing to:')
            tasks.edit(index, new_item)
        case 4:
            index = int(input('Moving which task?'))
            move_to = int(input('Moving to:'))
            tasks.rearrange(index, move_to)
print('See you next time!')

