name = {"ram","shyam","ravan"}

print(name)

name.add("sita")
print(name)

#you can use in and not in operator in set 

#name.remove("SITA") # remove data if present throw error if not 
name.discard("SITA") # remove data if presnet do nothing if not 

name.clear()

n1 = {1,3,4,5,7,8,9}
n2 = {1,2,3,4,5,11}

print(n1)
print(n2)
n3 = n1.union(n2)
print(n3)

print("******************")
n4 = n1.intersection(n2)
print(n1)
print(n2)
print(n4)

