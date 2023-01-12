
def is_prime(n):
  if n < 2:
    return False
  
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

print(is_prime(2))
print(is_prime(-3))
print(is_prime(0))
print(is_prime(1))
print(is_prime(4))

