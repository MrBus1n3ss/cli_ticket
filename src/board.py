from src import todo_controller as tc, todo as Todo


def filler_space(width: int, offset: int, *strings: str) -> str:
    count = 0
    for text in strings:
        count += len(text)
    return ' ' * (width - count - offset)


def complete_line():
    return f"|{'-' * (int(width/2) - 2)}|{'-' * (int(width/2) -2)}|"


def create_board(width: int, con, view="todo"):
    width = 100
    line = '-' * (width - 1)
    half_space = filler_space(int(width/2), -1, "todo", "done")
    print(line)
    print('| todo' + half_space + '| done' + half_space + '|')
    if view == "detail":
        pass
    elif view == "todo":
        buffer = get_tickets(width, con)
        for i in range(4, 20):
            print(buffer[i])
        print(line)
    elif view == "report":
        pass
    else:
        pass


def get_tickets(width: int, con) -> list:
    line = f"|{'-' * (int(width/2) - 2)}|{'-' * (int(width/2) -2)}|"
    todo_controller = tc.Todo_Controller(con)
    todos = todo_controller.get_all()
    need_to_do = []
    completed = []
    buffer = []
    for t in todos:
        ticket = Todo.Todo(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7])
        if ticket.is_done == '0':
            need_to_do.append(ticket)
        else:
            completed.append(ticket)
    buffer = format_for_swim_lane_ticket(width, need_to_do, completed, buffer)
    return buffer


def format_for_swim_lane_ticket(width: int, need_to_do: list, completed: list, buffer: list) -> list:
    line = f"|{'-' * (width - 2)}|"
    todo_count = len(need_to_do)
    completed_count = len(completed)
    count = 0
    half_width = int(width/2)
    if todo_count > completed_count:
        count = todo_count
    elif completed > todo_count:
        count = completed_count
    else:
        count = todo_count
    for i in range(0, count):
        if i > todo_count - 1:
            buffer.append(f"|{'-' * (half_width - 2)}|{'-' * (half_width -2)}|")
            buffer.append(f"|{filler_space(half_width, 23, "")}| [x] priority: {completed[i].priority} id: {completed[i].id}{filler_space(width, 23, str(completed[i].id))}|")
            buffer.append(f"|{filler_space(half_width, 14, "")}|     title: {completed[i].title}{filler_space(width, 14, str(completed[i].title))}|")
            buffer.append(f"|{filler_space(half_width, 19, "")}|     start date: {completed[i].start_date.date()}{filler_space(width, 19, str(completed[i].start_date.date()))}|")
        elif i > completed_count - 1:
            buffer.append(f"|{'-' * (int(width/2) - 2)}|{'-' * (int(width/2) -2)}|")
            buffer.append(f"| [ ] priority: {need_to_do[i].priority} id: {need_to_do[i].id}{filler_space(half_width, 23, str(need_to_do[i].id))}|{filler_space(int(width/2), 2, '')}|")
            buffer.append(f"|     title: {need_to_do[i].title}{filler_space(half_width, 14, str(need_to_do[i].title))}|{filler_space(half_width, 2, "")}|")
            buffer.append(f"|     start date: {need_to_do[i].start_date.date()}{filler_space(half_width, 19, str(need_to_do[i].start_date.date()))}|{filler_space(half_width, 2, "")}|")
        else:
            buffer.append(f"|{'-' * (int(width/2) - 2)}|{'-' * (int(width/2) -2)}|")
            buffer.append(f"| [ ] priority: {need_to_do[i].priority} id: {need_to_do[i].id}{filler_space(half_width, 23, str(need_to_do[i].id))}| [x] priority: {completed[i].priority} id: {completed[i].id}{filler_space(half_width, 23, str(completed[i].id))}|")
            buffer.append(f"|     title: {need_to_do[i].title}{filler_space(half_width, 14, str(need_to_do[i].title))}|     title: {completed[i].title}{filler_space(half_width, 14, str(completed[i].title))}|")
            buffer.append(f"|     start date: {need_to_do[i].start_date.date()}{filler_space(half_width, 19, str(need_to_do[i].start_date.date()))}|     start date: {completed[i].start_date.date()}{filler_space(half_width, 19, str(completed[i].start_date.date()))}|")
    return buffer

"""
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
"""
