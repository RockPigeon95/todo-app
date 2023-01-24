from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y - %H:%M:%S")
print("It is " + now)
while True:
    user_action = input("Type Add, Show, Edit, Complete, or Exit: ")
    user_action = user_action.strip().capitalize()

    if user_action.startswith('Add'):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo.capitalize())

        write_todos(todos)

    elif user_action.startswith('Show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}. {item}")

    elif user_action.startswith('Edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("New TODO: ")
            todos[number] = new_todo.capitalize() + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('Complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            print(f"Todo {todo_to_remove} has been removed from the list.")
        except ValueError:
            print("Please enter an item.")
            continue
        except IndexError:
            print("Item not found, try another item.")
            continue
    elif user_action.startswith('Exit'):
        break
    else:
        print("Command is not valid.")


print("Bye!")
