from datetime import datetime as dt
import os
import pygame
import sqlite3
import threading

pygame.mixer.init()

class TaskList():
    
    def __init__(self, db_name="tasks.db"):
        self.db_name = db_name
        # When the program starts, immediately check if the table exists.
        # If it doesn't, create it.
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    deadline TEXT NOT NULL
                )
            ''')
    
    def add(self, name: str, dl: str):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("INSERT INTO tasks (name, deadline) VALUES (?, ?)", (name, dl))
    
    def delete(self, task_id: int):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
 
    
    def edit(self, index: int, new_item: 'Item'):
        if index - 1 <= len(self.task_list) and index - 1 >= 0:
            self.task_list[index-1:index] = [new_item]

    
    # rearrange items in list
    def rearrange(self, index: int, move_to: int):
        if index - 1 <= len(self.task_list) and index - 1 >= 0 and move_to - 1 < len(self.task_list) and move_to - 1 >= 0:
            self.task_list.insert(move_to - 1, self.task_list[index - 1])
            self.task_list.pop(index - 1)

        else: 
            print('Invalid!')
        
    
    def get_all(self):
            items = []
            with sqlite3.connect(self.db_name) as conn:
                # Grab all tasks, automatically sorted by urgency!
                cursor = conn.execute("SELECT id, name, deadline FROM tasks ORDER BY deadline ASC")
                
                for row in cursor:
                    # row[0] is the ID, row[1] is the Name, row[2] is the Deadline String
                    deadline_obj = dt.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                    items.append(Item(row[1], deadline_obj, task_id=row[0]))
                    
            return items

class Item:
    def __init__(self, name: str, deadline: dt, task_id=None):
        self.id = task_id
        self.deadline = deadline
        if name is not None:
            self.name = name
    
    def editName(self, name):
        self.name = name
    
    def editTime(self, year:int, month:int, day:int, hour:int, minute:int):
        self.deadline = dt(year, month, day, hour, minute)
    
    def play_audio(self, path):
        basedir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(basedir, 'alarm.wav')
        if os.path.exists(path):
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()


    def alarm(self):
        now = dt.now()
        if now >= self.deadline:
            alarm_thread = threading.Thread(target=self.play_audio, daemon=True)
            alarm_thread.start()
            print('You missed a deadline!')
            return True
        return False
    
    def __str__(self):
        return self.name + " " + self.deadline.strftime('%Y-%m-%d %I:%M:%S')
