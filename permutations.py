class Solution:
  # Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
  # [1,2,3]
  def permute_distinct(self, nums: List[int]) -> List[List[int]]:
    res = []
    visited = [False] * len(nums)
    path = []

    def dfs():
      if len(path) == len(nums):  # we found a path, add to res
        res.append(path[:])
        return

      for i,num in enumerate(nums):
        if visited[i]: # we already visited this number, don't add because permutations are unique
          continue

        visited[i] = True
        path.append(num)  # add try
        dfs()

        visited[i] = False
        path.pop() # remove try

      dfs()
      return res


      #                                                                 []
      #                                                            /    |    \
      #  .append(num) -> [1]   .pop() -> []                       /     |     \
      #                                                          /      |      \
      #                                                         /       |       \
      #                                                        1        2        3       <- this is where dfs() is called in the recursive case
      #                                                      /   \     /  \                 when we are in the recursive call, meaning the base was not met yet we go down    path.append()
      # .append(num) -> [1,2]   .pop() -> [1]               /     \                         when when recursive call is done, meaning the base case was met we go up         path.pop()
      #                                                    /       \               
      #                                                   /         \         
      #                                                [1,2]       [1,3]
      #                                                  |           |               
      #                                                  |           |              
      # .append(num) -> [1,2,3]   .pop() -> [1,2]        |           |               
      #                                                  |           |         
      #                                               [1,2,3]      [1,3,2]
      # 
      # 
      # 
      # #

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
# [1,1,2]
  def permute_duplicates(self, nums: List[int]) -> List[List[int]]:
    res = []
    path = []
    counter = {num: 0 for num in nums}
    for num in nums:
        counter[num] += 1
    # counter = Counter(nums) from collections import Counter
    
    def dfs():
      if len(path) == len(nums):
        res.append(path[:])
        return
      
      # iterate over counter because counter gives us unique values
      # start: counter = {1: 2, 2: 1}
      # 1 or 2
      # nums could give us the same number in a row 1 1 2
      for num in counter: 
        if counter[num] > 0:  
          path.append(num)
          counter[num] -= 1
          dfs()
            
          
          print(num)
          path.pop()
          counter[num] += 1    
 
      dfs()
      return res