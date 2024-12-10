name = input('whats your name?: ')
print('\nhello', name.title(), " Welcome to your To Do List:")
#FIO - Find a way to loop the entire program 
rule_log = '\n type "add" to add a task to your list'
'\n type "del" to remove a task'
'\n type "view" to view your To Do List'
'\n type "done" to display your finished To Do List!'
print(rule_log)
action = input('\n->')
to_do = []
while 'done' not in action:
    if action == 'add':
        task_title = input('Give your task a title: ')
        task_desc = input('Give your task a short description: ')
        new_task = task_title, task_desc
        print(new_task, ' ready to add this task?')
        conf_add_task = input('(y or n): ')
        if 'y' in conf_add_task:
                to_do.append(new_task)
                print(to_do)
        if 'n' in conf_add_task:
            break
    if action == 'del':
        print(task_title, 'which task would you like to remove? (')
        del_action = input('type the task title: ')
        #figure it out from here - use dei_action to remove the input from the to_do list
    if action == 'view':
        print(to_do)
    if action == "done":
        print('Check out your To Do List', name.title(),)
        print('-' * 30)
        print(to_do)

   



     
            

