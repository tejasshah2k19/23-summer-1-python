str = input("Enter string") #royal edu 

str = str.lower() # lower()-> string convert lowecase 
count = 0 

for c in str:
    if c == 'a' or c == 'e' or c == 'i'  or c == 'o'  or c == 'u' :
        count = count + 1 

print("Total Vowels => ",count)


upperCount = 0 
str = input("Enter string") #royal edu 

# >= 'A' and <= 'Z' 

for c in str:
    if c.isupper() == True:
        upperCount = upperCount + 1  

print("total upper letters => ",upperCount)