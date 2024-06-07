'''Task class to define the attributes of each task. Each should have a title,
a description and when it is due'''


class Task:
    def __init__(self, task_title, task_description, task_due):
        self.task_title = task_title
        self.task_description = task_description
        self.task_due = task_due

    def __repr__(self):
        return (
            f"Task: {self.task_title} " 
            f"({self.task_description}), "
            f"Due: {self.task_due} "
        )
