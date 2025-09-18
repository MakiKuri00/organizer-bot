import datetime
import os

class TaskList:
    
    def __init__(self):
        self.task_list = []
    
    def add(self, item: 'Item'):
        self.task_list.append(item)
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
    
    #unfinished
    def save(self):
        f = open("data.txt", "w")
        f.write(self.__str__())
        f.close()

    def load(self):
        if os.path.exists("data.txt"):
            f = open("data.txt")
            for line in f:
                self.task_list.append(line)
            f.close()
        else:
            f = open("data.txt", "x")
            f.close()
        
    
    def __str__(self):
        output = ""
        for i in range(len(self.task_list)):
            output += f"{i+1}. {self.task_list[i]}\n"
        return output

class Item:
    name = ""
    order = -1
    
    def __init__(self, name: str, year: int, month: int, day: int, hour: int, minute: int):
        self.deadline = datetime.datetime(year, month, day, hour, minute)
        if name is not None:
            self.name = name
    
    def editName(self, name):
        self.name = name
    
    def editTime(self, year:int, month:int, day:int, hour:int, minute:int):
        self.deadline = datetime.datetime(year, month, day, hour, minute)
    
    def alarm(self):
        now = datetime.datetime.now()
        if now.hour == self.deadline.hour and now.minute == self.deadline.minute and now.year == self.deadline.year and now.month == self.deadline.month and now.day == self.deadline.day:
            #SoundEffect()
            pass
    
    def __str__(self):
        return self.name + " " + self.deadline.__str__()
    # todo: finish Tasks
            

    
