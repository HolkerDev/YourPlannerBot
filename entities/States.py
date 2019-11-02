import enum


class TaskStates(enum.Enum):
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2
    ABORTED = 3
