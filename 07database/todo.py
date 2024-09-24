from todo_helper import create_table, read_todos, add_todos, update_todo, delete_todo, close_connection


def main():
    run = 1
    create_table()

    while run:
        print("Press 1: To read all todos: ")
        print("Press 2: To add a new todo: ")
        print("Press 3: To update a  todo: ")
        print("Press 4: To delete a todo: ")
        print("Press 5: To exit: ")

        ch = input("Please enter your choice: ")

        if ch == "1":
            read_todos()
        elif ch == "2":
            new_todo = input("Enter new todo: ")
            add_todos(new_todo)
        elif ch == "3":
            updated_todo = input("Enter the updated todo: ")
            idx = input("Enter the id to todo: ")
            update_todo(idx, updated_todo)
        elif ch == "4":
            idx = input("Enter the id of todo to delete: ")
            delete_todo(idx)
        elif ch == "5":
            run = 0
    
    close_connection()



if __name__ == '__main__':
    main()