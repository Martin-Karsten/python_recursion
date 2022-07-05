# array = [
# [1, 2, 3, 4].
# [12, 13, 14, 5],
# [11, 16, 15, 6],
# [10, 9, 8, 7],
# ]
#  traverse in spiral order
# -> [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# #

class Solution:
  def spiralTraverse(self, array: list) -> list:
    res = []

    def traverse(startRow, endRow, startCol, endCol):
      if startRow > endRow or startCol >  endCol:
        return

    traverse(0, len(array), 0, len(array[0]))
    return res
