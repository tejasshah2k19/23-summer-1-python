

contacts = []  # global list , in which we store all the contact details 

c1 = {
    "name":"ram","contactNum":"234"
}

c2 = {
    "name":"ramanuj","contactNum":"234"
}

c3 = {
    "name":"raone","contactNum":"234"
}

c4 = {
    "name":"rock","contactNum":"234"
}

contacts.append(c1)
contacts.append(c2)
contacts.append(c3)
contacts.append(c4)


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
       # print(contacts)#  [ {name,contact},{name,contact}]
        print("NAME    CONTACT")
        for c in contacts:
            print(c.get("name"),"    ",c.get("contactNum"))#Ram 

    elif choice == 4:
        print("Enter name for search")#ram
        search = input() #ram 
        for c in contacts:
            if c.get("name").lower().startswith(search.lower()) :
                print(c.get("name"),"    ",c.get("contactNum"))#Ram 

    elif choice == 3:
        i=0
        found = False 
        print("Enter name for search")#ram
        search = input() #ram 
        for c in contacts:
            if c.get("name").lower() ==  search.lower()  :
                print(c.get("name"),"    ",c.get("contactNum"))#Ram 
                found = True 
                break
            i=i+1 
        if found == True:
            contacts.pop(i)
    elif choice == 0:
        exit(0)
    else:
        print("\nInvalid Choice PTA")