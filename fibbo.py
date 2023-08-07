#0 1
#a b 

#0 1 1 
#a b c   


#0 1 1 
#  a b    
 

#0 1 1 2 
#  a b c 

#0 1 1 2 
#    a b 

#0 1 1 2 3 
#    a b c 
 
  
#0 1 1 2 3  5  8  13   21 ...    

 
a=0
b=1

print(a," ",b,end="  ")


for i in range(1,6):
    c = a+b 
    print(c,end="  ")
    a=b
    b=c 
