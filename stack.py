# The functions associated with stack are:



# empty() – Returns whether the stack is empty – Time Complexity : O(1)
# size() – Returns the size of the stack – Time Complexity : O(1)
# top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
# push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
# pop() – Deletes the top most element of the stack – Time Complexity : O(1)



stack = [] 
  
stack.append('a') 
stack.append('b') 
stack.append('c') 
  
print('Initial stack') 
print(stack) 
 
print('\nElements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
  
print('\nStack after elements are poped:') 
print(stack) 