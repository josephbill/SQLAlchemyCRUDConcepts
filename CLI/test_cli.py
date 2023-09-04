import unittest
from cli import TodoApp

class TestTodoApp(unittest.TestCase):
    # set up 
    def setUp(self):
        self.app = TodoApp()

    def test_add_task(self):
        self.add.add_task("Test task")
        self.assertIn("Test Task", self.app.tasks)

    # have other test cases.
