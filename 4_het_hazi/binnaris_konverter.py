def converter(decimal_value):

  dividend = decimal_value

  divisor = 2
  binary_value = ""

  while(dividend >= 1):

    quotient = dividend // divisor
    binary_value = str(dividend % divisor) + binary_value
    binary = dividend % divisor

    print(f"{dividend}\t/ {divisor} = {quotient} \t {binary}".expandtabs( len(str(decimal_value)) + 2) )

    dividend //= divisor

  return binary_value

def main():
  print("Decimális -> bináris konverter")
  decimal_value = int(input("Adjon meg egy decimális számot: "))
  print("\n")

  print(f"\nBináris szám: {converter(decimal_value)}") 

if __name__ == "__main__":
  main()