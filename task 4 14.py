l=[]
n=int(input("Enter range:"))
i=0
for i in range(i,n):
    x= int(input("Enter a value: "))
    l.append(x);
l.sort()
print(f"The second smallest number is {l[1]}")
