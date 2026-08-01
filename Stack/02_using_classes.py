class Stack():

    def __init__(self):
        self.stack =[]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        if len(self.stack)==0:
            return "Stack is Empty"
        else:
            return "Stack is not Empty"
        
    def __str__(self):
        return str(self.stack)
        

st = Stack()
st.push(10)
st.push(20)
st.push(30)

st.pop()
print(st)
print(f"The last element of stack is {st.peek()}")
print(st.isEmpty())