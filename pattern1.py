print("\n#########################\n")
"""
*s
**
***
****
*****

"""

for r in range(1,6):#r ->5-> time     r=1     r=2      r=3         r=4         r=5 
   for c in range(1,r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print("*",end="") 
   print("")

print("\n#########################\n")


"""
1
12
123
1234
12345 

"""
for r in range(1,6):#r ->5-> time     r=1     r=2      r=3         r=4         r=5 
   for c in range(1,r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print(c,end="") 
   print("")



print("\n#########################\n")
"""
1
22
333
4444
55555

"""

for r in range(1,6):#r ->5-> time     r=1     r=2      r=3         r=4         r=5 
   for c in range(1,r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print(r,end="") 
   print("")




print("\n#########################\n")
"""
1
23
456
78910
1112131415

"""
x = 1 
for r in range(1,6):#r ->5-> time     r=1     r=2      r=3         r=4         r=5 
   for c in range(1,r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print(x,end="")
      x=x+1  
   print("")

