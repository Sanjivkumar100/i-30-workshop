marks=float(input("Enter student mark:"))
if marks>90:
    print('grade:O')
elif marks>81 and marks<90:
    print('grade:A')
elif marks>71and marks<80:
    print('grade:B')
elif marks >61 and marks<70:
    print('grade:C')
elif marks >51 and marks<60:
    print('grade:D')
else:
    print("U")
