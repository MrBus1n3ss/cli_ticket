def filler_space(width: int, offset: int, *strings: str) -> str:
    count = 0
    for text in strings:
        count += len(text)
    return ' ' * (width - count - offset)


def line(width: int, offset: int) -> str:
    return '-' * (width - offset)


def header(title: str, width: int):
    l = f"|{'-' * (width - 2)}|"
    print(l)
    # TODO: add date time and project (project is later
    print(f"| Date: {title} Time: {filler_space(width, 0, "")}|")
    print(f"| {title}{filler_space(width, 3, title)}|")
    print(l)
