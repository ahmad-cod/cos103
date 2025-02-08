def is_prime(num):
  # if num is less than 2 return false
  # if num is divisible by any number less than it return false
  if num < 2:
    return False
  half = num // 2
  for i in range(2, half + 1):
    if num % i == 0:
      return False
    
  return True

print(is_prime(18))
    