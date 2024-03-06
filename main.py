nric = input('Enter an NRIC number: ')

# Type your code below

if nric.startswith('T' or 'G'): #doesn't work for more than  1 argument
  print("prefix valid")

digits = nric[1:8]
if digits.isdigit():
  print("digits are valid")

suffix = nric[-1]
if suffix.isalpha():
  print("suffix valid")