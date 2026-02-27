from datetime import datetime as dt
import os
import winsound as wsnd
import csv
import threading

class TaskList:
    
    def __init__(self):
        self.task_list = []
    
    def add(self, name: str, dl: dt):
        item = Item(name, dt.strptime(dl, '%Y-%m-%d %I:%M:%S'))
        self.task_list.append(item)
        print(self.task_list)
        #self.__str__()
    
    def delete(self, index: int):
        if index - 1 <= len(self.task_list) and index - 1 >= 0:
            self.task_list.pop(index -1)
            #self.__str__()
    
    def edit(self, index: int, new_item: 'Item'):
        if index - 1 <= len(self.task_list) and index - 1 >= 0:
            self.task_list[index-1:index] = [new_item]
            #self.__str__()
    
    # rearrange items in list
    def rearrange(self, index: int, move_to: int):
        if index - 1 <= len(self.task_list) and index - 1 >= 0 and move_to - 1 < len(self.task_list) and move_to - 1 >= 0:
            self.task_list.insert(move_to - 1, self.task_list[index - 1])
            self.task_list.pop(index - 1)
            #self.__str__()
        else: 
            print('Invalid!')
    
    def to_csv_list(self, task_list):
        csv_list = []
        for i in task_list:
            csv_list.append([i.deadline.strftime('%Y-%m-%d %I:%M:%S'), i.name])
        print(csv_list)
        return csv_list
    
    def save(self):
        with open("data.csv", "w", newline='') as f:
            writer = csv.writer(f)
            csv_list = self.to_csv_list(self.task_list)
            writer.writerows(csv_list)

    def load(self):
        with open("data.csv", "r") as f:
            content = csv.reader(f)
            for line in content:
                self.task_list.append(Item(line[1], dt.strptime(line[0], '%Y-%m-%d %I:%M:%S')))
            print(self.task_list)
        
    
    def __str__(self):
        output = ""
        for i in range(len(self.task_list)):
            output += f"{i+1}. {self.task_list[i]}\n"
        return output

class Item:
    def __init__(self, name: str, deadline: dt):
        self.deadline = deadline
        if name is not None:
            self.name = name
    
    def editName(self, name):
        self.name = name
    
    def editTime(self, year:int, month:int, day:int, hour:int, minute:int):
        self.deadline = dt(year, month, day, hour, minute)
    
    def play_audio(self, path):
        try:
            wsnd.PlaySound(path, wsnd.SND_FILENAME | wsnd.SND_NODEFAULT)
        except Exception as e:
            print(f"\nAlarm Error: {e}")

    # def alarm(self):
    #     now = dt.now()
    #     if now >= self.deadline:
    #         basedir = os.path.dirname(os.path.abspath(__file__))
    #         path = os.path.join(basedir, 'alarm.wav')
    #         alarm_thread = threading.Thread(target=self.play_audio, args=(path))
    #         alarm_thread.start()
    #         print('You missed a deadline!')
    
    def __str__(self):
        return self.name + " " + self.deadline.strftime('%Y-%m-%d %I:%M:%S')
            

    
