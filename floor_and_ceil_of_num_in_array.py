# Given a sorted integer array, find the floor and ceiling of a given number in it.
# The floor and ceiling map the given number to the largest previous or the smallest following integer in the array.

# nums = [1, 4, 6, 8, 9]
# Number 5 —> ceiling is 6, floor is 4
# Number 6 —> ceiling is 6, floor is 6
class Solution:
  def findCeiling(nums: list, left: int, right: int, target: int) -> int:
    if not nums:
      return - 1

      if target <= nums[left]:
        return nums[left]

      if target > nums[right]:
        return - 1

      mid = (left + right) // 2

      if nums[mid] == target:
        return nums[mid]

      elif nums[mid] < target:
        return findCeiling(nums, mid + 1, right, x)

      else:
        return findCeiling(nums, left, mid, x)

  def findFloor(nums: list, left: int, right: int, target: int) -> :
    if not sums:
      return - 1

    if target < nums[left]:
      return - 1

    if target >= nums[right]:
      return nums[right]

    mid = (left + right) // 2

    if nums[mid] == target:
      
