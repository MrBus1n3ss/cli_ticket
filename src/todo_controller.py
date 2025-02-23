from src import todo as Todo


class Todo_Controller:
    def __init__(self, con):
        self.con = con
        self.cur = con.cursor()

    def create(self, todo: Todo.Todo):
        with self.con:
            self.con.execute("""INSERT INTO todo(
                                    title,
                                    priority,
                                    project,
                                    completed,
                                    description,
                                    start_date,
                                    finish_date)
                                 VALUES(?, ?, ?, ?, ?, ?, ?)""",
                             (todo.title,
                              todo.priority,
                              todo.project,
                              False,
                              todo.description,
                              todo.start_date,
                              None))
            self.con.commit()

    def get_all(self) -> list:
        return self.cur.execute("SELECT * FROM todo").fetchall()

    def get_one_by_id(self, id: int):
        print(id)
        return self.cur.execute("SELECT * FROM todo WHERE id=?", (id,)).fetchone()

    def get_by_project(self, project: str) -> list:
        return self.cur.execute("SELECT * FROM todo WHERE project=?", (project,)).fetchall()

    def get_by_priority(self, priority: int) -> list:
        return self.cur.execute("SELECT * FROM todo WHERE priority=?", (priority,)).fetchall()

    def get_by_start_date(self, start_date) -> list:
        return self.cur.execute("SELECT * FROM todo WHERE start_date > ?", (start_date,)).fetchall()

    def update(self, todo: Todo.Todo):
        with self.con:
            self.cur.execute("""UPDATE todo
                                 SET
                                    title = ?,
                                    priority = ?,
                                    project = ?,
                                    completed = ?,
                                    description = ?,
                                    start_date = ?,
                                    finish_date = ?
                                 WHERE id = ?""",
                             (todo.title,
                              todo.priority,
                              todo.project,
                              todo.is_done,
                              todo.description,
                              todo.start_date,
                              todo.finish_date,
                              todo.id))

    def delete(self, id):
        self.cur.execut("DELETE FROM todo where id=?", (id,))
