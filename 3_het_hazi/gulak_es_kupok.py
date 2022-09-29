import math

PI = 3.14

def kor():
  r = float(input("Adja meg a kör sugarát: "))
  kor_terulet = math.pi * r * r

  print(f"Kör területe: {kor_terulet} cm\u00B2")

  return kor_terulet

def teglalap():
  print("Adja meg a teglalap két oldalát!")

  a = float(input("A oldal: "))
  b = float(input("B oldal: "))
  teglalap_terulet = a * b

  print(f"Téglalap területe: {teglalap_terulet} cm\u00B2")

  return teglalap_terulet


def gula_vagy_kup_terfogat():

  gula_vagy_kup = input("gúla vagy kúp?: ")
  alap_terulet = teglalap() if gula_vagy_kup == "gúla" else kor()

  m = float(input("Adja meg a kúp magasságát: "))
  gula_vagy_kup_terfogat = (1 / 3) * alap_terulet * m

  print(f"A gúla vagy kúp térfogata: {gula_vagy_kup_terfogat} cm\u00B3")

def main():
  gula_vagy_kup_terfogat()

if __name__ == "__main__":
  main()