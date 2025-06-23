import curses


def run():
    # t1 = threading.Thread(target=loop, args=('test',))
    # t1.start()
    t3 = threading.Thread(target=main_loop)
    t3.start()
    # t2 = threading.Thread(target=spinner)
    # t2.start()


def loop(print_screen: str):
    while True:
        print(print_screen)
        user_input()


def main_loop():
    stdscr = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()
    curses.curs_set(1)
    window = curses.newwin(0, 0)
    x = 0
    y = 0
    try:
        while True:
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
            window.addstr(0, 0, "Test", curses.color_pair(1))
            c = window.getch()
            if c == ord('j'):
                if y < window.getmaxyx()[0] - 1:
                    window.addstr(2, 0,  str(window.getmaxyx()), curses.color_pair(1))
                    y += 1
                window.move(y, 0)
            if c == ord('k'):
                if y > 0:
                    window.addstr(2, 0,  str(window.getmaxyx()), curses.color_pair(1))
                    y -= 1
                window.move(y, 0)
            if c == ord('l'):
                if x < window.getmaxyx()[1] - 1:
                    window.addstr(2, 0,  str(window.getmaxyx()), curses.color_pair(1))
                    x += 1
                window.move(0, x)
            if c == ord('h'):
                if x > 0:
                    window.addstr(2, 0,  str(window.getmaxyx()), curses.color_pair(1))
                    x -= 1
                window.move(0, x)

            window.addstr(1, 0,  str(window.getyx()), curses.color_pair(1))

            # window.refresh()
    except KeyboardInterrupt:
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        print('Stopped by user')
    finally:
        curses.endwin()

# May keep this, just wanted to created a spinner
def spinner():
    spinner = ['/', '|', '\\', '-']
    while True:
        for spin in spinner:
            print(spin)


def user_input():
    return input('=>')
