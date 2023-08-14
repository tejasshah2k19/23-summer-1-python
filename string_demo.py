#name = input() 
"""
    this is multiline comment 
"""

'''
    this is also multiline comment 
'''

name = "royal"

print(name) # royal  #01234  

print(len(name))

"""
    we can access single character using index 
    index starts with 0 
    and ends with SIZE-1

"""
print(name[0]) # r 
print(name[1]) # o 
print(name[2]) # y 
print(name[3]) # a 
print(name[4]) # l 

print("======================")
i = 0 
while i < len(name):
    print(name[i])
    i=i+1

print("======================")
for c in name:
    print(c)


print("======================")
for i in range(0,len(name)):
    print(name[i])

"""
    python supports negative indexing 
    python supports slicing 
"""   

print("======================")
name = "gabbar" 
print(name[0])# g 
print(name[-1])  # end => r
print(name[-2])  # end => a 
print(name[-3])  # end => b 
print(name[-4])  # end => b 
print(name[-5])  # end => a 
print(name[-6])  # end => g 


print("======================")
name = "gabbar" 

print(name[0:4]) # 0123 

print(name[0:5:2]) # 024 gba 



