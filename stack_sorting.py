# Stack before sorting : [5, -2, 9, -7, 3]
# Stack after sorting  : [-7, -2, 3, 5, 9]

class Solution:
  def sortedInsert(self, stack, key):
  
      # base case: if the stack is empty or
      # the key is greater than all elements in the stack
      if not stack or key > stack[-1]:
          stack.append(key)
          return
  
      ''' We reach here when the key is smaller than the top element '''
  
      # remove the top element
      top = stack.pop()
  
      # recur for the remaining elements in the stack
      self.sortedInsert(stack, key)
  
      # insert the popped element back into the stack
      stack.append(top)

  # Recursive method to sort a stack
  def sortStack(self, stack):
  
      # base case: stack is empty
      if not stack:
          return
  
      # remove the top element
      top = stack.pop()
  
      # recur for the remaining elements in the stack
      self.sortStack(stack)

      print(stack, top)
  
      # insert the popped element back into the sorted stack
      self.sortedInsert(stack, top)

      return stack

sol = Solution()

sol.sortStack([5, -2, 9, -7, 3])