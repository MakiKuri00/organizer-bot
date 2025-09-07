import datetime

class TaskList:
    
    def __init__(self):
        self.task_list = []
    
    def add(self, item):
        self.task_list.append(item)
        self.__str__()
    
    def delete(self, index: int):
        if index - 1 <= len(self.task_list) and index - 1 >= 0:
            self.task_list.pop(index -1)
            self.__str__()
    
    def edit(self, index: int, new_item: str):
        if index - 1 <= len(self.task_list) and index - 1 >= 0:
            self.task_list[index-1:index] = [new_item]
            self.__str__()
    
    # rearrange items in list
    def rearrange(self, index: int, move_to: int):
        if index - 1 <= len(self.task_list) and index - 1 >= 0 and move_to - 1 < len(self.task_list) and move_to - 1 >= 0:
            self.task_list.insert(move_to - 1, self.task_list[index - 1])
            self.task_list.pop(index - 1)
            self.__str__()
    
    def __str__(self):
        for i in range(len(self.task_list)):
            print(i + 1, '. ', self.task_list[i], '\n')

class Tasks:
    name = ""
    order = -1
    
    def __init__(self, name, year: int, month: int, day: int, hour: int, minute: int):
        self.deadline = datetime.datetime(year, month, day, hour, minute)
        if name is None:
            self.name = name
    
    def editName(name):
        self.name = name
    
    def editTime(year:int, month:int, day:int, hour:int, minute:int):
        self.deadline = datetime.datetime(year, month, day, hour, minute)
    
    def alarm():
        now = datetime.datetime.now()
        if now.hour == deadline.hour and now.minute == deadline.minute and now.year == deadline.year and now.month == deadline.month and now.day == deadline.day:
            SoundEffect()
    
    # todo: finish Tasks
            

    
