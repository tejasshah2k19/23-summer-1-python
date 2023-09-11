
user = {
	"firstName":"rock",
	"email":"rock@www.com",
	"age":55,
    "age":25
}


print(user) #json 
print(user["email"])
print(user.get("email"))
print(len(user))
print(user.keys())

print("age" in user)

user.update({"email":"john@www.com"})
user.update({"password":"1111"})
print(user)
user.pop("password")
print(user)