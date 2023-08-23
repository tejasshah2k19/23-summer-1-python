def add(a=50,b=20):
    print("a => ",a)
    print("b => ",b)
    print(a+b)


add(15,20) #positional argument 
#add() #error
#default argument
add()#a->50 b->20

add(500) #a->500 b->20 

add(b=1,a=2) #name argument 



#create one function isEven() that takes num as argument 
#and return true if number is even 
#and return false if number is odd 


def isEven(num):
    if int(num%2) == 0:
        return True
    else:
        return False 
    
ans = isEven(7)
print(ans)


print(isEven(20))