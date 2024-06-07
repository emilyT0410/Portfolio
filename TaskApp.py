"""Task app class which handles user management"""

from TaskList import TaskList


class TaskApp:

    # Blank dictionary to store registered user log in details
    login_details_dict = {"a": "test"}  # Test user log in details

    # Instance of task list
    task_list = TaskList()

    def register(self) -> None:
        """Guest user creates an account"""
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        if username in self.login_details_dict:
            print("Username already taken")
        else:
            self.login_details_dict[username] = password
            print(f"Hi {username}, your account has been created successfully")

    def get_user_login(self):
        """Get user to input username and password"""
        user_username = input("Enter your username: ")
        user_password = input("Enter your password: ")
        # Validate log in details
        return self.validate_user_login(user_username, user_password)

    def validate_user_login(self, user_username, user_password):
        """Validate user log in details"""
        if user_password == self.login_details_dict.get(user_username):
            print("Log in successful")
            return True
        else:
            print("Incorrect username or password. Please try again")
            return False

    def quit(self) -> None:
        """Quits application"""
        print("Bye!")
        exit(0)

    def initial_menu(self) -> None:
        """Initial menu (before user has logged in)"""
        print("\nMenu options:")
        print("1. Create account")
        print("2. Log in")
        print("3. Quit application\n")

    def run(self) -> None:
        """Runs application"""
        while True:
            # initial menu presented to user
            self.initial_menu()
            # User prompted to select an option
            user_option = int(input("Please select an option from the menu "))
            if user_option == 1:
                self.register()  # User creates account
            elif user_option == 2:
                while True:
                    if self.get_user_login():  # User logs in
                        self.task_list.run()
            elif user_option == 3:
                self.quit()  # Quit application
            else:
                # If option outside of menu is selected return error
                print("Error: That is not a menu option. Try again.")
