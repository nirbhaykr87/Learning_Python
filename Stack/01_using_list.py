
# Implementing Stack using List

stack = []  

stack.append(10)  # pushing the elements in Stack
stack.append(20)
stack.append(30)

stack.pop()    # Poping the element

print(f"Your stack is : {stack}")

print(f"The top element is : {stack[-1]}")   # peek ( gives you the top element of the stack)

if len(stack)==0:
    print("Stack is empty")
else:
    print("Stack is not empty")
