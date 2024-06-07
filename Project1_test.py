import unittest
from TaskList import TaskList
from TaskApp import TaskApp


class TestTaskListDeleteTask(unittest.TestCase):
    """Test the functionality of the delete task function"""

    def test_delete_with_valid_index(self):
        task_list = TaskList()
        """USE CASE 1: Test with valid index"""
        # Arrange
        value = 0  # Index 0 - remove the only item in list
        # Act
        self.assertEqual(len(task_list.task_list), 1)  # Task list length = 1
        task_list.delete_task(value)
        # Assert
        self.assertEqual(len(task_list.task_list), 0)  # Task list length = 0

    def test_delete_with_invalid_index(self):
        task_list = TaskList()
        """USE CASE 2: Test with invalid index"""
        # Arrange
        value = 1  # Index 1 
        # Act
        self.assertEqual(len(task_list.task_list), 1)  # Task list length = 1
        with self.assertRaises(IndexError):  # Asserting an Index Error
            task_list.delete_task(value)
        # Assert
        self.assertEqual(
            len(task_list.task_list), 1
        )  # Expect the result to be 1 as nothing removed


class TestTaskListAddTask(unittest.TestCase):
    """Test the add task function"""

    def test_add_task_with_input(self):
        task_list = TaskList()
        """USE CASE 3: Test with given input"""
        # Arrange
        task_title = "Task title"
        task_description = "Task description"
        task_due = "Deadline"
        value = (task_title, task_description, task_due)
        # Act
        self.assertEqual(len(task_list.task_list), 1)  # Task list length = 1
        task_list.add_task_to_list(value)
        # Assert
        self.assertEqual(len(task_list.task_list), 2)  # Task list length = 2


class TestTaskAppValidateUserLogIn(unittest.TestCase):
    """Test the validate user log in function"""

    def test_validate_user_log_in_with_valid_details(self):
        """USE CASE 4: Test with valid test user details"""
        task_app = TaskApp()
        # Arrange
        username = "a"
        password = "test"
        # Act
        result = task_app.validate_user_login(username, password)
        # Assert
        self.assertTrue(result)  # Log in correct so result True

    def test_validate_user_log_in_with_invalid_details(self):
        """USE CASE 5: Test with invalid test user details"""
        task_app = TaskApp()
        # Arrange
        username = "wrong"
        password = "wrong"
        # Act
        result = task_app.validate_user_login(username, password)
        # Assert
        self.assertFalse(result)  # Log in incorrect so result False


if __name__ == "__main__":
    unittest.main()
