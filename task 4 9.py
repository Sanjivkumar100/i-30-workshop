
def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=i
    print(f"factoial of {n}:{factorial}")

a=int(input("Enter a number:"))
fact(a)
