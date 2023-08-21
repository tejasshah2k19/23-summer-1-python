str = "royal"

print(str.upper()) # upper case 
print(str.lower()) # lower case 

print(str.capitalize()) #title case 

print(str.count("a"))

#email = "tejas@gmail.com"
#email  ="rock@yopmail.com" #email -> it may be in upper - lower - or mix 
email = "rocky@GMAil.Com"
#gmail -> 
#take email from user and print valid if its valid gmail 
#print invalid if its not valid gmail account 


#end -> @gmail.com 
if(email.lower().endswith("@gmail.com") and len(email) >= 13):
    print("Valid")
else:
    print("InValid")

#startswith() 

#str.isalnum() -> return true if all characters are {a-zA-Z0-9}
#isalpha() -> return true if all characters are {a-zA-Z}

