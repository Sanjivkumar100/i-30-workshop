l1=[]
l2=[]
l3=[]
def fl(n):

    print("elements for first list")
    for i in range(1,n+1):
        inp=int(input(f"Enter element {i}:"))
        l1.extend([inp])
def sl(n):
   
    print("elements for Second list")
    for i in range(1,n+1):
        inp=int(input(f"Enter element {i}:"))
        l2.extend([inp])
def ml(l1,l2):
    
    for j in range(len(l1)):
        if (l1[j]%2)!=0:
            l3.extend([l1[j]])
    for k in range(len(l2)):
        if (l2[k]%2)==0:
            l3.extend([l2[k]])
    print(f"Merged list:{l3}")

n=int(input("Enter a range:"))
fl(n)
sl(n)
ml(l1,l2)

