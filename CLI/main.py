# argparse is how you will request inputs from the user 
# action attribute , to set a Flag. 
import argparse
from cli import TodoApp

# instance
app = TodoApp()

parser = argparse.ArgumentParser(description="Simple To-Do List Manager")
parser.add_argument("-a", "--add", help="Add a task to the to-do list")
parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
parser.add_argument("-r", "--remove", type=int, help="Remove a task by its index")
args = parser.parse_args()


#  test cases.
if args.add:
    app.add_task(args.add)
elif args.list:
    print(app.list_tasks())
elif args.remove:
    print(app.remove_task(args.remove))
else: 
    print("No valid command issued to our CLI app.")


# to run the commands 
# python main.py followed by action term : followed by any necessary arguemnets 