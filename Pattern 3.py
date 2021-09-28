row=int(input("Enter a row:"))
k=2*row-2
for i in range(0,row):
    for j in range(0,k):
        print(end=" ")
    k-=1
    for l in range(0,i+1):
        print('*',end=' ')
    print("\r")

