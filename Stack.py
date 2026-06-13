#CREATE AN CLASS STACK  WITH POP AND PUSH FUNCTION
class stack:
    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values = [x] + self.values
    def pop(self):
        return self.values.pop(0)   

#CREATE AN EMPTY STACK 
S = stack()

#INSERT SOME DATA INTO THE STACK USING PUSH FUNCTION
S.push(10)
S.push(20)
S.push(30)
S.push(40)

#PRINT THE STACK
print(S.values)

#DELETE ANY DATA FROM THE STACK USING POP FUNCTION
S.pop()
print(S.values)

#PUSH ANY DATA INTO THE STACK 
S.push(50)
print(S.values)
