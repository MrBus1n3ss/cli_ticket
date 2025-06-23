import sys
import uuid
import sqlite3
from datetime import datetime


class Project:
    def __init__(self,
                 id: uuid,
                 name: str,
                 description: str,
                 created_at: datetime,
                 modified_at: datetime):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.modified_at = modified_at


class Ticket:
    def __init__(self,
                 id: uuid,
                 project_id: uuid,
                 name: str,
                 description: str,
                 priority: int,
                 state: str,
                 created_at: datetime,
                 modified_at: datetime):
        self.id = id
        self.project_id = project_id
        self.name = name
        self.description = description
        self.state = state
        self.created_at = created_at
        self.modified_at = modified_at


def build_tables(con):
    with open("tables.sql", 'r') as statement:
        lines = statement.readlines()
        for line in lines:
            con.execute(line)
            con.commit()


def create_project(name: str):
    project_id = str(uuid.uuid4())
    project_name = ""
    description = ""
    created_at = datetime.now()


def get_project():
    pass


def update_project():
    pass


def delete_project():
    # TODO: need to check if tickets exist in project
    pass


def main():
    con = sqlite3.connect("tickets.db", detect_types=sqlite3.PARSE_DECLTYPES)
    build_tables(con)
    # print(con.execute("SELECT * FROM state").fetchall())
    args = sys.argv
    if len(args) > 1:
        command = args[1]
        match command:
            case "project":
                try:
                    operation = args[2]
                    match operation:
                        case "create":
                            print("create")
                        case "update":
                            print("update")
                        case "get":
                            print("get")
                        case "delete":
                            print("delete")
                except Exception:
                    print("Missing arguments")
                    sys.exit(0)
            case "ticket":
                try:
                    operation = args[2]
                    match operation:
                        case "create":
                            print("create")
                        case "update":
                            print("update")
                        case "get":
                            print("get")
                        case "delete":
                            print("delete")
                except Exception:
                    print("Missing arguments")
                    sys.exit(0)

    else:
        print("No args selected")
        sys.exit(0)


if __name__ == "__main__":
    main()
