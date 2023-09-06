list = ["ram","shyam","ganshyam"]

print(list)

print(list[0])

print(list[0:2]) #0 1 

print(list[-1]) # last element 


print("ram" in list)  #True 
print("ravan" in list) #False

print("ram" not in list) # False 


list[0] = "RAM"

print(list)


#insert an item at given location 

list.insert(0,"sita")
print(list)

list.append("ravan")
print(list)

#list.remove("ram") #RAM 
#print(list)


list.pop(0)  # remove 0th index 

#list.clear() # remove all items from the list 


#duplicate 
#index 
#value modify 
#unsorted  

# list.sort()

list.sort(reverse=True)
print(list)

