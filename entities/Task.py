from entities import States
from datetime import datetime


class Task:
    assigned = list()
    state = States.TaskStates.TODO
    name = str()
    id = int()
    create_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    deadline = None
    points = int()
    description = str()

    def __init__(self, name, deadline, description):
        self.name = name
        self.deadline = deadline
        self.description = description

    def add_assigned(self, names):
        self.assigned.append(names)

    def start_task(self):
        self.state = States.TaskStates.IN_PROGRESS

    def done_task(self):
        self.state = States.TaskStates.DONE

    def abort_task(self):
        self.state = States.TaskStates.ABORTED

    def save_task(self, tasks_len):
        self.id = tasks_len + 1
