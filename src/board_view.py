def filler_space(width: int, offset: int, *strings: str) -> str:
    count = 0
    for text in strings:
        count += len(text)
    return ' ' * (width - count - offset)


def line(width: int, offset: int) -> str:
    return '-' * (width - offset)


def detail_view(title: str, width: str):
    print('| {todo} |')


def todo_view():
    pass


def todo_view_buffer(width: int, need_to_do: list, completed: list, buffer: list) ->:
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



def report_view():
    pass


