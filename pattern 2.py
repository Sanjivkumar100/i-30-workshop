def starrow(n):
    for i in range(n):
        print('*',end='')

rows=int(input("Enter the numbers of rows:"))
for i in range(1,rows+1):
    starrow(i)
    print()
