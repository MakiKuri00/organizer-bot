from datetime import datetime as dt
import pygame
import sqlite3

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
 
    
    def edit(self, task_id: int, name: str, dl: str):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("UPDATE tasks SET name = ?, deadline = ? WHERE id = ?", (name, dl, task_id))
        
    def get_one(self, task_id: int):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute(
                "SELECT id, name, deadline FROM tasks WHERE id = ?", (task_id,)
            )
            row = cursor.fetchone()
            if row is None:
                return None
            deadline_obj = dt.strptime(row[2], '%Y-%m-%d %H:%M:%S')
            return Item(row[1], deadline_obj, task_id=row[0])

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
