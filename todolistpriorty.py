todolisthig=[]
todolistmed=[]
todolistlow=[]
def hightask():
    task=input("Enter the new task:")
    todolisthig.append(task)
    print(todolisthig)
def medtask():
    task=input("Enter the new task:")
    todolistmed.append(task)
    print(todolistmed)
def lowtask():
    task=input("Enter the new task:")
    todolistlow.append(task)
    print(todolistlow)
def edithig():
  newtask=input("Enter the new task")
  oldtask=input("Enter old task:")
  indexno=todolisthig.index(oldtask)
  todolisthig[indexno]=newtask
  print(todolisthig)

def editmed():
  newtask=input("Enter the new task")
  oldtask=input("Enter old task:")
  indexno=todolistmed.index(oldtask)
  todolistmed[indexno]=newtask
  print(todolistmed)

def editlow():
  newtask=input("Enter the new task")
  oldtask=input("Enter old task:")
  indexno=todolistlow.index(oldtask)
  todolistlow[indexno]=newtask
  print(todolistlow)
def deletehig():
    task=input("Enter the task:")
    todolisthig.remove(task)
    print(todolisthig)
def deletemed():
    task=input("Enter the task:")
    todolisthig.remove(task)
    print(todolistmed)
def deletelow():
    task=input("Enter the task:")
    todolistlow.remove(task)
    print(todolistlow)
