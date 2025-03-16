class Menus:

    def __init__(self):
        self.menu = []

    def add(self, menu):
        self.menu.append(menu)

    def pop(self):
        if len(self.menu) > 0:
            self.menu.pop()
