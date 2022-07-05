class Solution:
  def find_floor(self, array: list, target: int) -> int:
    if not array:
      return - 1

    def find_floor_helper(array, target, left, right):
      if array[left] < target:
        return -1

      if array[right] >= target:
        return array[right]

      mid = (left + right) // 2

      if mid == left:
        return array[mid]

      if array[mid] == target:
        return array[mid]
      elif array[mid] > target:
        return find_floor_helper(array, target, left, mid - 1)
      elif array[mid] < target:
        return find_floor_helper(array, target, mid, right)

    return find_floor_helper(array, target, 0, len(array) - 1)

  def find_ceil(self, array: list, target, left, right):
    if not array:
      return - 1

    def find_ceil_helper(array, target, left, right):
      if array[right] > target:
        return -1

      if array[left] <= target:
        return array[left]

      mid = (left + right) // 2

      if mid == right:
        return array[mid]

      if array[mid] == target:
        return array[mid]
      elif array[mid] > target:
        return find_ceil_helper(array, target, mid + 1, right)
      elif array[mid] < target:
        return find_ceil_helper(array, target, left, mid)

      return find_ceil_helper(array, target, 0, len(array) + 1)

