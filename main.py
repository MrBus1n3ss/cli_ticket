import sys
import sqlite3
from datetime import datetime
from src import board, todo, todo_controller
from pynput.keyboard import Key, Listener


def build_tables(con):
    with open("tables.sql", 'r') as statement:
        with con:
            con.execute(statement.read())


def parse_user_input():
    user_input = input('=>')


def main():
    width = 100
    con = sqlite3.connect("tickets.db", detect_types=sqlite3.PARSE_DECLTYPES)
    board.create_board(width, con)
    """
    build_tables(con)
    """
    mock_todo = todo.Todo(None, "Test", 1, "test_project", "A test call", False, datetime.now(), None)
    tc = todo_controller.Todo_Controller(con)
    tc.create(mock_todo)
    """
    todos = []
    for t in tc.get_all():
        print(len(t))
        todos.append(todo.Todo(t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7]))
    # board.create_board()
    todos[len(todos)-1].is_done = True
    print(todos[len(todos)-1].is_done)
    tc.update(todos[len(todos)-1])
    print(type(todos[len(todos)-1].id))
    print(tc.get_one_by_id(int(todos[len(todos)-1].id)))
    """
    con.close()


if __name__ == "__main__":
    main()
