Tasks_all = []
print('Welcome')
print('please choose an option')

if __name__ == '__main__':
    while True:
        print('1.Add to list')
        print('2.Add to delete')
        print('3.List of tasks')
        print('4.Quit')

        selection = input('please select a number and write it here: \n')

        if selection == '1':
            task_to_do = input('please make a name for your task: \n')


            def Add_tasks(task_to_do):
                Tasks_all.append(task_to_do)
                print(f'Task {Tasks_all.index(task_to_do) + 1}: {task_to_do} , added to list of tasks \n ')


            Add_tasks(task_to_do)

        elif selection == '2':
            try:
                task_to_delete = int(input('please choose the number of task to delete:\n'))


                def Add_delete(task_to_delete):
                    if 1 <= task_to_delete <= len(Tasks_all):
                        Tasks_all.pop(task_to_delete - 1)
                        print(f'task is removed')
                    else:
                        print('please Enter a valid number of tasks')


                Add_delete(task_to_delete)

            except:
                print('wrong number\n')

        elif selection == '3':
            def show_list(Tasks_all):
                for words in Tasks_all:
                    print(f'{Tasks_all.index(words) + 1}: {words}\n')


            show_list(Tasks_all)

        elif selection == '4':
            def Quit_list():
                print('BuyBuy')


            Quit_list()
            break


    else:
        print('invalid input')


