from math import factorial
from factorial import Factorial

def test_factorial():
  factorial = Factorial()
  assert (factorial.fact(4) == 24)

  # fact(4) = 4 * fact(3) * 3 * fact(2) * 1

if __name__ == "__main__":
  test_factorial()
  print('tests passed')
  