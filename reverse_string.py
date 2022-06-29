# given a string s return the reversed string
# example input: hello
# example output: olleh
class Solution:
  def reverse_string(self, s: str) -> str:
    if not s:
      return ''

    self.reversedString = ''
    def reverse(s: str, index: int):
      if index < 0:
        return self.reversedString

      self.reversedString += s[index]
      reverse(s, index - 1)

    reverse(s, len(s) -1)
    return self.reversedString

  def reverse_string(self, s: str) -> str:
    if not s:
      return ''

    def reverse(s: str, reversedString: str, index: int) -> str:
      if index < 0:
        return reversedString

      reversedString += s[index]
      return reverse(s, reversedString, index - 1)

    return reverse(s, '', len(s) - 1)

# how to solve this problem
  # divide problem into sub problems
  # what are we returning? void or value
  # find easiest to solve sub problem
    # -> base case
      # return void or value
  # find recursive case

