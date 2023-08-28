colors = ['red','green']
numbers = []
print(colors)
print(numbers)
print(colors[0]) #red 
print(colors[1]) #green 
print(len(colors))


#how to add  new data in list 
numbers.append(10) # end of the list 
numbers.append(20)
numbers.append(5)

print(numbers) # 10 20 5 

print("All the numbers from list -> ")
for num in numbers:
    print(num)


#take 5 numbers from user and print it 

list = []
sum = 0 
print("How many numbers you want to add")
size = int(input())

for i in range(1,size+1):
    print("Enter number")
    num = int(input())
    list.append(num)

print("All numbers")
for n in list:
    print(n)
    sum = sum + n 

print("total sum => ",sum)

#take n numbers from user and find out max from it 
#take n numbers frrom user and search number from n numbers 

