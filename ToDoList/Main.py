import time
import os

liner = "\033[33m____________________________________\033[0m"

all_tasks = []


def save_to_file():
    with open('tasks.txt', 'w') as file:
        for item in all_tasks:
            file.write(item + '\n')


def read_file():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            for item in file:
                all_tasks.append(item.strip())


read_file()

print('Welcome to my task list')
print(liner)
if __name__ == "__main__":

    while True:
        time.sleep(0.75)
        print('List of commands: 😊\n')
        print('\033[34m1. To add a task\033[0m')
        print('\033[34m2. To delete a task\033[0m')
        print('\033[34m3. To show all tasks\033[0m')
        print('\033[34m4. To quit the app\n\033[0m')
        selection = input("Please choose a number to proceed: \n"
                          "Enter Here: \033[31m>>\033[0m ")
        print(liner)

        if selection == '1':
            task_to_add = input('Create a name for your task: ')

            def add_tasks(task_to_add):
                all_tasks.append(task_to_add)
                print(f"Task #{all_tasks.index(task_to_add)+ 1} called {task_to_add.upper()} is added to your main tasklist")
                print(liner)
                save_to_file()
            add_tasks(task_to_add)
        elif selection == '2':
            try:
                task_to_delete = int(input('Which task would you like to delete? Enter the number. \n'
                                           'Here: '))
                print(liner)

                def delete_task(task_to_delete):
                    if 1 <= task_to_delete <= len(all_tasks):
                        all_tasks.pop(task_to_delete - 1)
                        print(f'Task #{task_to_delete} is removed.')
                        print(liner)
                    elif task_to_delete <= 0:
                        print('\033[31mA task number cannot be smaller than 1.\033[0m')
                        print(liner)
                    else:
                        print(f'\033[31mTask does not exist. You have only {len(all_tasks)} item(s) in the list\033[0m')
                        print(liner)
                delete_task(task_to_delete)
            except ValueError:
                print('\033[33mPlease enter a task number.\033[0m')
                print(liner)

        elif selection == '3':
            if all_tasks == []:
                print('\033[31mYou need to first create at least one task, then I can show you a list.\033[0m')
                print(liner)
            else:
                def list_tasks(all_tasks):
                    print('Here is a list of you current tasks:')
                    for task in all_tasks:
                        print(f'\033[1;32m{all_tasks.index(task) + 1}. {task}\033[0m')
                    print(liner)
                list_tasks(all_tasks)

        elif selection == '4':
            def quit_app():
                print('Bye Bye! 💋')
                print('See you next time!')
            quit_app()
            break

        else:
            print('\033[31mInvalid input, please enter a number. Thanks!! 👍\033[0m')
            print(liner)
