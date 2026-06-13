class person():
    def __init__(lol,name,age=18):
        lol.name = name
        lol.age = age

    def greet(lol):
        print("Hello")
        print("How are you " + lol.name)

p1 = person("aryan")
p2 = person("Reeyansh",21)

print(p1.name)
print(p1.age)
p1.greet()
print(p2.name)
print(p2.age)
p2.greet()
