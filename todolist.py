from todolistpriorty import hightask,lowtask,medtask,edithig,editlow,editmed,deletehig,deletelow,deletemed  
def addtask():
    add={1:hightask,2:medtask,3:lowtask}
    print("Choose the priority level\n\tPress 1 High\n\tPress 2 Medium \n\tPress 3 Low ")
    while True:
        options=int(input("Enter your choice: "))
        if options in add:
            action=add[options]
            action()
        elif options==0:
            break;
def edittask():
    edit={1:edithig,2:editmed,3:editlow}
    print("Choose the priority level\n\tPress 1 High\n\tPress 2 Medium \n\tPress 3 Low ")
    while True:
        options=int(input("Enter your choice: "))
        if options in edit:
            action=edit[options]
            action()
        elif options==0:
            break;
def delete():
    delete={1:deletehig,2:deletemed,3:deletelow}
    print("Choose the priority level\n\tPress 1 High\n\tPress 2 Medium \n\tPress 3 Low ")
    while True:
        options=int(input("Enter your choice: "))
        if options in delete:
            action=delete[options]
            action()
        elif options==0:
            break;

actions={1:addtask,2:edittask,3:delete}

while True:
    print("Todolist App\n\tPress 1 to add new task\n\tPress 2 to edit the task \n\tPress 3 to delete the task ")
    choice=int(input("Enter your choice: "))
    if choice in actions:
        action=actions[choice]
        action()
    elif choice==0:
        break;

