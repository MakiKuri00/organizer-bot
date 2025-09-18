import os
import datetime
import Tasks
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

curr_list = Tasks.TaskList()
curr_list.load()

#App Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Robot Companion")
main_window.resize(640, 480)

#Objects/Widgets
curr_time = datetime.datetime.now()
if curr_time.hour > 6 and curr_time.hour < 12:
    welcome_msg = QLabel("Good morning! What would you like to do?")
elif curr_time.hour > 12 and curr_time.hour < 18:
    welcome_msg = QLabel("Good afternoon! What would you like to do?")
else:
    welcome_msg = QLabel("Good evening! What would you like to do?")

curr_task_msg = QLabel("Here are your ongoing tasks:")

task_list = QLabel(curr_list.__str__())

op1 = QPushButton("Add")
op2 = QPushButton("Delete")
op3 = QPushButton("Edit")

#Design
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()

row1.addWidget(welcome_msg, alignment=Qt.AlignCenter)

row2.addWidget(curr_task_msg, alignment=Qt.AlignTop) # Alignment may need to be changed later

row3.addWidget(task_list, alignment=Qt.AlignCenter)

row4.addWidget(op1)
row4.addWidget(op2)
row4.addWidget(op3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)
master_layout.addLayout(row4)

main_window.setLayout(master_layout)

#Exec
main_window.show()
app.exec_()

#Implement button functions


#Primitive code logic
# HIGHEST_COMMAND_NUM = 4
# print('Welcome to Organizer Bot!')

# command = int(input('[1]: Add a task \n[2]: Delete a task \n[3]: Edit a task \n[4]: Rearrange tasks \n[5]: Exit'))
# tasks = Tasks.TaskList()
# while command != 5:
#     match command:
#         case 1:
#             item = input('Enter a new task:')
#             tasks.add(item)
#         case 2:
#             index = int(input('Which task do you want to remove?'))
#             tasks.delete(index)
#         case 3:
#             index = int(input('Choose a task to edit:'))
#             new_item = input('Changing to:')
#             tasks.edit(index, new_item)
#         case 4:
#             index = int(input('Moving which task?'))
#             move_to = int(input('Moving to:'))
#             tasks.rearrange(index, move_to)
# print('See you next time!')

