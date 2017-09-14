def read_todos():
    with open("todos.txt", "r") as file_reader:
        print(file_reader.read())

def main():
   
    print("Here are my todos:")
    
    read_todos()
    user_input = raw_input("Press 1 to add a todo or 2 to delete a todo: ")

    if user_input == "1":
        new_todo = raw_input("Enter your new todo: ")
        # Note that 'r' and 'a' are options for open(...)
        with open("todos.txt", "a") as file_appender:
            file_appender.write("\n" + new_todo)
        print("New todo added: ")
        read_todos()
    else:
        delete_todo = raw_input("Enter which todo to delete: ") + "\n"
        f = open("todos.txt", "r")
        lines = f.readlines()
        f.close()

        f = open("todos.txt", "w")
        for line in lines:
            if line != delete_todo:
                f.write(line)
        f.close()

        f = open("todos.txt", "r")
        print("Thanks for deleting! Here is the updated version of the todo list:\n" + f.read())

if __name__ == '__main__':
    main()