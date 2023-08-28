#take n numbers from user and find out max from it 
list = []
n = int(input("How many numbers you want to take?"))
for i in range(1,n+1):
    print("Enter value")
    list.append(int(input())) 

#25 63 65 45 85 96 21 
max = list[0]
for n in list: 
    if n > max :
        max = n 
print("max = ",max)

#take n numbers frrom user and search number from n numbers 
search = int(input("Enter number that you want to search"))
found = False # not found 
for n in list: 
    if n == search:
        found = True 

if found  == True:
    print("Number found")
else:
    print("Number not found")

if search in list:
     print("Number Found....")
else:
    print("Number Not found....")

    