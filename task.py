

#1) print 1 to 20 using for loop 


for i in range(1,21): #i=i+1  
    print(i)

#1) print 1 3 ,5 ,7 ..... 20 using for loop  
for i in range(1,21,step=2): #i = i + 2 
    print(i)



#2) ask start number and end from user and print all numbers between start and end 
start = int(input("Enter Start number"))
end = int(input("Enter End number"))

for i in range(start,end+1):
    print(i)


#3) take number from user and print multiplication table of that number 
num = int(input("Enter number"))

for i in range(1,11):
    print(num," * ",i," = ",num*i) #5 * 1 = 5 





#4)1 -2 3 -4 5 -6 7 -8 
num = int(input("Enter end number"))
for i in range(1,num+1):
    if i % 2 == 0:
        print("-",i,end=" ")  
    else:
        print(i,end=" ")   
   
#5) num = 4 => 1 4 9 16 
num = int(input("Enter end number"))
for i in range(1,num+1):
    print(i*i,end=" ")#1 4 9 16 25 
 





