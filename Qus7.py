class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def celebrate_birthday(self):
        self.age += 1
        print("happy birthday you are now" , self.age)

p1 = person("Reeyansh",19)
print(p1.name)
p1.celebrate_birthday()




