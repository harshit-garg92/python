def greet(name):
    return "hello, " + name 

a = input("name:")
if not a:
    print("hello user")
else:
    print(greet(a))

#def greet(name = "User"):
    #return "hello" + name

#print(greet("chai"))
#print(greet())
