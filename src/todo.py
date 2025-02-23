from datetime import datetime


class Todo:
    def __init__(self,
                 id: int,
                 title: str,
                 priority: int,
                 project: str,
                 description: str,
                 is_done: bool,
                 start_date: datetime,
                 finish_date: datetime):
        self.id = id
        self.title = title
        self.priority = priority
        self.project = project
        self.description = description
        self.is_done = is_done
        self.start_date = start_date
        self.finish_date = finish_date

    def __str__(self):
        return f'id: {self.id}, title: {self.title}, priority: {self.priority}, project: {self.project}, description: {self.description}, is_done: {self.is_done}, start_date: {self.start_date}, finish_date: {self.finish_date}'
