"""Tasklist class. This class handles all the
functions to do with the task list"""

from Task import Task


class TaskList:

    def __init__(self):
        """Function initialises the empty task list and
        populates list with test task upon start up"""
        self.task_list = []

        task = Task("Test Task", "This is a test", "Today")
        self.task_list.append(task)  # Populates with test task

    def which_task_delete(self) -> int:
        """Function asks the user which task they want to delete
        and stores that value as idx"""
        while True:
            user_idx = int(input("Which number task would you like to delete? "))
            idx = user_idx - 1
            try:
                self.validate_user_input(idx)  # Check task is in the list
                return idx
            except IndexError as e:
                print(f"Error: {e}")  # Returns error

    def validate_user_input(self, idx: int) -> None:
        """Function validates the user input, checking the value
        chosen is within the range of the length of list"""
        if idx not in range(len(self.task_list)):
            raise IndexError(
                f"Task doesn't exist: There are only {len(self.task_list)} tasks"
            )

    def delete_task(self, idx: int) -> None:
        """Deletes task"""
        task = self.task_list[idx]
        self.task_list.remove(task)  # remove task from list using idx

    def view_task_list(self) -> None:
        """Views task list"""
        print("Task list: ")
        # Add numbers to tasks, starting at 1
        for count, task in enumerate(self.task_list, start=1):
            print(count, task)

    # Empty list to add completed tasks to
    completed_tasks = []

    def which_task_complete(self) -> int:
        """Function asks the user which task they want to complete
        and stores that value as idx"""
        while True:
            user_idx = int(input("Which number task would you like to complete? "))
            idx = user_idx - 1
            try:
                self.validate_user_input(idx)  # Check task is in the list
                return idx
            except IndexError as e:
                print(f"Error: {e}")  # Flag error and ask again

    def mark_task_complete(self, idx: int) -> None:
        """Marks task as complete"""
        task = self.task_list[idx]
        self.task_list.remove(task)  # Remove task from list using idx
        self.completed_tasks.append(task)  # Add task to completed list

    def view_completed_tasks(self) -> None:
        """Views completed tasks in a list"""
        print(self.completed_tasks)

    def create_new_task(self) -> None:
        """Creates a new task"""
        # Prompt the user to add title and description
        task_title = input("Add task title: ")
        task_description = input("Add description: ")
        task_due = input("Add deadline: ")
        task = Task(task_title, task_description, task_due)
        self.add_task_to_list(task)

    def add_task_to_list(self, task):
        """Adds task to list"""
        self.task_list.append(task)

    def quit(self) -> None:
        """Quits application"""
        print("Bye!")
        exit(0)

    def task_list_menu(self) -> None:
        """Task list menu (after user has logged in)"""
        print("\nMenu options:")
        print("1. Create task")
        print("2. View task list")
        print("3. Complete task")
        print("4. View completed tasks")
        print("5. Delete task")
        print("6. Quit application\n")

    def run(self) -> None:
        """Function which run the task list"""
        while True:
            # initial menu presented to user
            self.task_list_menu()
            # User prompted to select an option
            user_option = int(input("Please select an option from the menu "))
            if user_option == 1:
                self.create_new_task()  # Create new task
            elif user_option == 2:
                self.view_task_list()  # View task lists
            elif user_option == 3:
                idx = self.which_task_complete()
                self.mark_task_complete(idx)  # Completes task
            elif user_option == 4:
                self.view_completed_tasks()  # Shows completed task list
            elif user_option == 5:
                idx2 = self.which_task_delete()
                self.delete_task(idx2)  # Delete task from list
            elif user_option == 6:
                self.quit()  # Quit application
            else:
                # If option outside of menu is selected return error
                print("Error: That is not a menu option. Try again.")
