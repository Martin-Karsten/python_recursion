class Solution:
  #   [-7, -2, 5, 9, 3]
  def sum_array(self, array: list) -> int:
    if not array:
      return 0

    el = array.pop()
    # recursion done. return base case
      # self.sum_array(array) 0 + el -> 0 + (-7) = -7
    # second recursive step
      # self.sum_array(array) -7 + el -2 = -9
    # third recursive step
      # -9 + el ...
    # el + [n:el] el + rest of the array excluding el
    return self.sum_array(array) + el


    