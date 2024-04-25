#creating a stack
originalStack=[]
originalStack.append("Yvonne")
originalStack.append("Leila")
originalStack.append("Martin")
originalStack.append("Josphine")
print(originalStack)#output:['Yvonne', 'Leila', 'Martin', 'Josphine']

#removing an item in a stack
newStack=originalStack.pop()
print(newStack)#output:Yvonne

#adding an item in a stack
stack=originalStack.append("Kenya")
print(stack)
print(originalStack)#output:['Leila', 'Martin', 'Josphine', 'Kenya']


#accessing an item in  a stack
stack2=originalStack[2]
print(stack2)#output:Josphine

newstack1=[]
newstack1.append("cow")
newstack1.append("cat")
newstack1.append("giraffe")
print(newstack1)

newstack1.pop()
print(newstack1)
print(type(newstack1))

class stack(object):

    def __init__(self):
        self.items=[]

    def push(self,item):
        ''' this will remove last item
        :return:none
        '''

        self.items.append(item) 
    def pop(self):
        '''Allow us to see the Last elements
        :return:Last item'''
        self.item.pop()
        pass
    def peek(self):
        if self.item:
          return self.items[-1]
        else:
            return None
    
    def size (self):
        if self.item:
            return len(self.item)
        else:
            return None
        
    def isempty(self):
        if self.item==[]:
          return True
        else:
          return False
if __name__=="_main_":
    stack=stack()
    stack.push("1")
    stack.push("2")
    print(stack.size())
    print(stack.peek())

    stack.pop()
    print(stack.size())
    print(stack.peek())

    print(stack.isempty())
    stack.pop()
    print(stack.isempty())