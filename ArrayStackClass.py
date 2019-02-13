class ArrayStack:
#constractor of the list 
    def __init__(self):
        self.data =[] #creat empty stack
        
    #retutn the number of elments in the stack
    def __len__(self):
        return len(self.data)
    
    #check if the stack is empty 
    def is_empty(self):
        return self.data ==0
       # if self.data ==0 :
         #   return true
       # else:
         
    #new element will store at the end of the stack
    def push(self,e):
        self.data.append(e)
    #return (but not remove the elment at the top of the stack
    def top(self):
        if self.is_empty():
            raise Empty("stack is empty")
        return self.data[-1]
    
    ##remove and return the element from the top pf stack 
    def pop(self):
        if self.is_empty():
            raise Empty("stack is empty")
        return self.data.pop()  
         
stack1=ArrayStack() #creat a new stack and take object from class 
stack1.push(5) #add 5
stack1.push(6) #add 6
print(stack1.__len__()) #print the length of the stack
print(stack1.pop()) #deldet elment 
print(stack1.__len__()) #print the length of the stack

