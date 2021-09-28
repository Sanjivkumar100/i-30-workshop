def addcontact():
    name=input('Enter name:')
    phoneno=int(input("Enter phone number"))
    contactbook[name]=phoneno
def deletecontact():
    name=input("Enter the name to delete:")
    del contactbook[name]
    print(contactbook)
def editcontact():
    name=input('Enter name:')
    phoneno=int(input("Enter phone number"))
    contactbook[name]=phoneno
def searchcontact():
    name=input('Enter name:')
    if  name in contactbook:
        print(f"Number={contactbook[name]}")
def show():
    print(contactbook)

contactbook={}
directory={1:addcontact,2:deletecontact,3:editcontact,4:searchcontact,5:show}
choice=0
while True:
    print("Contact directory App\n\tPress 1 to add new number\n\tPress 2 to delete the number \n\tPress 3 to edit the number\n\tPress 4 to search the number \n\tPress 5 to show the number")
    choice=int(input("Enter your choice: "))
    if choice in directory:
        book=directory[choice]
        book()
    elif choice==0:
        break;

