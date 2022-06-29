class Factorial:
  def fact(self, num: int) -> int:
    if num == 1:
      return 1
    
    return num * self.fact(num -1)