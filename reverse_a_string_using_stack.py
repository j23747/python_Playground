# # Python program to reverse a string using stack
 
# # Function to create an empty stack.
# # It initializes size of stack as 0
# def createStack():
#     stack=[]
#     return stack
 
# # Function to determine the size of the stack
# def size(stack):
#     return len(stack)
 
# # Stack is empty if the size is 0
# def isEmpty(stack):
#     if size(stack) == 0:
#         return true
 
# # Function to add an item to stack .
# # It increases size by 1
# def push(stack,item):
#     stack.append(item)
 
# #Function to remove an item from stack.
# # It decreases size by 1
# def pop(stack):
#     if isEmpty(stack): return
#     return stack.pop()
 
# # A stack based function to reverse a string
# def reverse(string):
#     n = len(string)
     
#     # Create a empty stack
#     stack = createStack()
 
#     # Push all characters of string to stack
#     for i in range(0,n,1):
#         push(stack,string[i])
 
#     # Making the string empty since all
#     #characters are saved in stack
#     string=""
 
#     # Pop all characters of string and
#     # put them back to string
#     for i in range(0,n,1):
#         string+=pop(stack)
         
#     return string
     
# # Driver program to test above functions
# string="GeeksQuiz"
# string = reverse(string)
# print("Reversed string is " + string)
 

class Solution(object):
    def calculate(self, s):
         """
         :type s: str
         :rtype: int
         """
         stack = []
         num = 0
         sign = "+"
         for c in s:
            if c.isdigit():
                 num = num * 10 + int(c)
            if c in ["+", "-", "*", "/"]:
                if sign == "+":
                     stack
                    elif sign == "-":
                        stack.append(-num)
                    elif sign == "*":
                        stack.append(stack.pop() * num)
                    elif sign == "/":
                        stack.append(int(stack.pop() / num))
                        return sum(stack)
                    sign = c
                    num = 0
            return sum(stack)


