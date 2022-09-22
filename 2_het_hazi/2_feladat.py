from cmath import sqrt
import math



def pythagoras():
  print("Pitagorasz-tétel")
  print("Adja meg az A és B oldalt, válaszul a C oldalt kapja meg.")
  a = int(input("A oldal: "))
  b = int(input("B oldal: "))

  c = math.sqrt(a ** 2 + b ** 2)

  print(f"A C oldal: {round(c)}")

def quadratic_equation():
  print("Másodfokú egyenlet")
  print("Adjon meg 3 számot!")
  a = int(input("a: "))
  b = int(input("b: "))
  c = int(input("c: "))

  x1 = 0
  x2 = 0

  d = b * b - 4 * a * c

  if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"x\u2081: {x1}")
    print(f"x\u2082: {x2}")
  elif d == 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    print(f"x\u2081, X\u2082: {x1}")
  else:
    print("Nincs megoldása a valós számok között.")

def is_prime():
  print("Prím szám-e")
  number = int(input("Adjon meg egy számot, hogy megnézze prímszám-e: "))

  if number > 1:
    for i in range(2, number):
      if number % i == 0:
        print(f"A(z) {number} nem egy prímszám.")
        break
    else:
        print(f"A(z) {number} egy prímszám.")
  else:
    print("Az 1 nem egy prímszám.")

def main():
  
  pythagoras()
  print("---------------------")
  quadratic_equation()
  print("---------------------")
  is_prime()
  print("---------------------")

if __name__ == "__main__":
  main()