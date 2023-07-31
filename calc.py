print("Enter TWo numbers")
n1 = int(input())  #float 
n2 = int(input())

print("1 For Add\n2 For Sub\n3 For Mul\n4 For Div\nEnter your choice")
choice = int(input())

if choice == 1 :
    ans = n1 + n2 
    print("addition = ",ans)

elif  choice == 2:
    ans = n1 - n2 
    print("subtraction = ",ans)

elif choice == 3:
    ans = n1 * n2 
    print("multiplication = ",ans)

elif choice == 4:
    ans = n1 / n2 
    print("division = ",ans)
else:
    print("Invalid choice")