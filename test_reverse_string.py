from reverse_string import Solution

def test_reverse_string():
  solution = Solution()
  assert solution.reverse_string('hello') == 'olleh'
  assert solution.reverse_string('12') == '21'
  assert solution.reverse_string('123') == '321'
  assert solution.reverse_string('') == ''
  assert solution.reverse_string('1') == '1'

if __name__ == "__main__":
  test_reverse_string()
  print('tests passed')