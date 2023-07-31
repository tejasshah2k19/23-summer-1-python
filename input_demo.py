import datetime 


print("Enter Name : ")
name = input() # scanf cin 
print("Enter CityName : ")
city = input() 
print("Enter Born Year : ")
year = int(input()) #1947->string  

currentYear = datetime.date.today().year 

age = currentYear - year 


print("Name : ",name)
print("City : ",city)
print("Age  : ",age)