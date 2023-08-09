print("\n#########################\n")
"""
*
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
A : 65 
AB  6566  
ABC 656667 
ABCD
ABCDE 6566676869 

"""
for r in range(65,70):#r ->5-> time     r=1     r=2      r=3         r=4         r=5 
   for c in range(65,r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print(chr(c),end="") 
   print("")



print("\n#########################\n")
"""
    *
   **
  ***
 ****
*****

"""

for r in range(1,6):#r ->5-> time     r=1     r=2      r=3         r=4         r=5 
   for s in range(1,6-r):
      print(" ",end="")
   for c in range(1,r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print("*",end="") 
   print("")


print("\n#########################\n")
"""
    *
   **
  ***
 ****
*****

"""

for r in range(1,6):#r ->5-> time     r=1     r=2      r=3         r=4         r=5 
   for s in range(1,6-r):
      print(" ",end="")
   for c in range(1,r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print("*",end="") 
   print("")


print("\n#########################\n")
"""
    *
   * *
  * * *
 * * * *
* * * * *

"""

for r in range(1,6):#r ->5-> time     r=1     r=2      r=3         r=4         r=5 
   for s in range(1,6-r):
      print(" ",end="")
   for c in range(1,r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print("* ",end="") 
   print("")



print("\n#########################\n")
"""

*****
****
***
**
*

"""

for r in range(1,6):#r    r=1     r=2      r=3         r=4         r=5 
    for c in range(1,6-r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print("*",end="") 
    print("")





print("\n#########################\n")
"""

*****
 ****
  ***
   **
    *

"""

for r in range(1,6):#r    r=1     r=2      r=3         r=4         r=5 
    for s in range(1,r):
       print(" ",end="")
    for c in range(1,6-r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print("*",end="") 
    print("")




print("\n#########################\n")
"""

* * * * *
 * * * * 
  * * *
   * *
    *

"""

for r in range(1,6):#r    r=1     r=2      r=3         r=4         r=5 
    for s in range(1,r):
       print(" ",end="")
    for c in range(1,6-r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print("* ",end="") 
    print("")





print("\n#########################\n")
"""
    *
   * * 
  * * * 
 * * * * 
* * * * *
 * * * * 
  * * *
   * *
    *

"""

for r in range(1,5):#r ->5-> time     r=1     r=2      r=3         r=4         r=5 
   for s in range(1,6-r):
      print(" ",end="")
   for c in range(1,r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print("* ",end="") 
   print("")

for r in range(1,6):#r    r=1     r=2      r=3         r=4         r=5 
    for s in range(1,r):
       print(" ",end="")
    for c in range(1,6-r+1):#c-> 5->time c=1     c=1 2    c=1 2 3     c=1 2 3 4   c=1 2 3 4 5 
      print("* ",end="") 
    print("")

