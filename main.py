# Modules
import itertools
from decimal import Decimal

# Returns an 8-bit binary
def denaryToBinary(n):  
    binary = bin(n).replace("0b", "")
    while len(binary) != 8:
      binary = "0" + binary
    return binary

def main(num): 
  # Convert denary to float and then to fraction
  try:
    denary = float(num)
  except:
    print("The input could not be converted to a float.")
    exit()

  fraction = denary.as_integer_ratio()
  numerator = fraction[0]
  denominator = fraction[1]

  # Convert to proper fraction
  no_division = 0
  while abs(numerator) > denominator:
    denominator = denominator * 2
    no_division += 1

  # Calculate Mantissa
  sequence = [-1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128]
  for i in range(len(sequence)):
    for j in itertools.combinations(sequence, i):
        if sum(j) == numerator/denominator:
          mantissa_fractions = j
          
  # Round decimal
  try:
    mantissa_fractions
  except:
    # Round to binary form
    decimal = Decimal(str(denary)) % 1
    print(decimal)
    decimal = decimal * -1
    print(decimal)
    binary_decimal = ""
    for i in range(8):
      decimal = decimal * 2
      if decimal > 1:
        binary_decimal += "1"
      else:
        binary_decimal += "0"
      decimal = Decimal(str(decimal)) % 1
    final_binary_decimal = str(denaryToBinary(int(denary))) + str(binary_decimal)
    for i in range(len(final_binary_decimal)):
      if final_binary_decimal[i] == "1":
        firstOne = i
        break
    rounded = True
    
      
    # Convert binary mantissa to denary
    binary_mantissa = final_binary_decimal[firstOne-1:firstOne+8]
    exponent = len(final_binary_decimal)-8-firstOne
    mantissa = 0
    for i in range(len(binary_mantissa)) :
      if i == 0 and binary_mantissa[i] == "1" :
          mantissa = -1
      elif binary_mantissa[i] == "1" :
          mantissa = mantissa +  1/(2**i)
    
    rounded_denary = mantissa * 2**exponent
    
    if denary < 0: 
      rounded_denary = rounded_denary * -1
    
    denary = rounded_denary

    
    main(denary)
    
  # Check if the mantissa is positive or negative
  binary_mantissa = ""
  current_fraction = mantissa_fractions[0].as_integer_ratio()
  if current_fraction == (-1,1):
    binary_mantissa += "1"
    beginAt = 1
  else:
    binary_mantissa += "0"
    beginAt = 0

  # Create binary
  current_denominator = 2
  match = False
  for i in range(1,8):
    match = False
    for j in range (beginAt,len(mantissa_fractions)):
      current_fraction = mantissa_fractions[j].as_integer_ratio()
      if current_fraction[1] == current_denominator:
        match = True

    if match == True:
      binary_mantissa += "1"
    else:
      binary_mantissa += "0"
    current_denominator = current_denominator * 2

  # Output
  if float(initial_input) != denary : print("\nThe denary number was rounded to", denary)
  print(f"\n{denary} = {fraction[0]}/{fraction[1]} = {numerator}/{denominator} * 2^{no_division}\n")
  print("Mantissa:", binary_mantissa )
  print("Exponent: " + denaryToBinary(no_division)+"\n")

  answer = input("Continue? (y/n) ")
  if answer == "yes" or answer == "y":
    main(input("\n> "))
  else:
    exit()

print("\nWelcome to floating point denary to binary converter.")
print("=====================================================")
print("\nEnter the denary number to convert.\n")

initial_input = input("> ")
main(initial_input)

