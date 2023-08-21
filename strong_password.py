password = input("Enter Password")

length = 0  # < 8 
upper = 0   #  0 -> upper is missing 1-> upper is present  
lower = 0 
digit = 0 


if len(password) >= 8 :
    length = 1 


for c in password:
    if c.isupper():
        upper = 1 
    elif c.islower():
        lower= 1 
    elif c.isdigit():
        digit = 1 
""" 
	strong -> if it contains 
						1 capital
						1 lower 
						1 digit 
						>= 8 in length 
		normal -> if it contains 
						>= 8 in length
						any of two from {1 lower, 1 upper, 1 digit }
		weak -> if it is < 8 length 
				  
		weak -> it contains only lower or only upper or only digit 
"""
if length == 0:
    print("WEAK")
elif length == 1 and upper == 1 and lower == 1 and digit == 1:
    print("STRONG")
elif length == 1 and  ( ( upper + lower + digit ) == 2 ) :
    print("NORMAL")
elif (upper+lower+digit) == 1 :
    print("WEAK")

