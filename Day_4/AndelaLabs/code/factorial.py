def factorial(number):
  #initialize the
  fnumber = 1
  while number > 0:
      fnumber = fnumber * number
      number = number - 1
  return fnumber