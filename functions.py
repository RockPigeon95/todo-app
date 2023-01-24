FILE_PATH = "todos.txt"


def get_todos(filepath=FILE_PATH):
    """Read a text file and return a list of todos items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_l, filepath=FILE_PATH):
    """Write a todos items list in a text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_l)

