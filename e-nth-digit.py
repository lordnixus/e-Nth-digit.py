import decimal

def compute_e():
  n = int(input("Enter the number of digits after the decimal point: "))
  decimal.getcontext().prec = n+1
  e = decimal.Decimal(1).exp()
  return e

print(compute_e())
