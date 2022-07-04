from floor_and_ceil_of_num_in_array import Solution

def test_floor_and_ceil_of_num_in_array():
  solution = FloorAndCeil()
  assert (solution.floor_and_ceil([[1, 4, 6, 8, 9], 5]) == [4,6])

if __name__ == "__main__":
  test_floor_and_ceil_of_num_in_array()
  print('tests passed')
  