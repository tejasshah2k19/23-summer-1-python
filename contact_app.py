

contacts = []  # global list , in which we store all the contact details 


while True: 
    print("Press 1 For New Contact\nPress 2 For List\nPress 3 For Delete Contact\n4Press For Search Contact")
    print("\n0 For Exit\nEnter Your choice")

    choice = int(input()) 

    if choice == 1 :
        name = input("Enter name")
        contactNum = input("Enter Contact Num")
        c = {"name":name,"contactNum":contactNum}
        contacts.append(c)
    elif choice == 2:
        print(contacts)
    elif choice == 3:
        pass
    elif choice == 4:
        pass 
    elif choice == 0:
        exit(0)
    else:
        print("\nInvalid Choice PTA")