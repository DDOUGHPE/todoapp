name = input('whats your name?: ')
print('\nhello', name.title(), " Welcome to your To Do List:")
direc_list = print('\n type "add" to add a task to your list'
'\n type "del" to reomve a task'
'\n type "view" to view your To Do List'
'\n type "done" to display your finished To Do List!')
action = input('\n->')
to_do = []
for action in action:
    if 'add' in action:
        while action == "done":
            
        add_to_do = to_do.append(input("what task will you like to add" + ' ' + name.title() + '?: '))
        print(to_do)
        if 'done' or "view" in add_to_do:
            print("here is" + "" + name + " 's Complete To-Do List!")
            print(to_do)
            break
        continue
    if 'del' in action:
        print(to_do, '\n what would you like to delete?', name.title, "?")
    if 'view' in action:
        print(to_do)
    if 'done' in action:
        print("here's ypur list:" + '\n',  to_do)
else:
    print('invaild selection')
