def plusrow():
    print("+",end=' ')
    for i in range(4):
        print('-',end=' ')
    print('+',end=' ')
    for i in range(4):
        print('-',end=' ')
    print('+')

def otherrow():
    print('|',end=' ')
    for i in range(4):
        print(' ',end=' ')
    print('|',end=' ')
    for i in range(4):
        print(' ',end=' ')
    print('|')

for i in range(1,12):
    if i==1 or i==6 or i==11:
        plusrow()
    else:
        otherrow()
     
