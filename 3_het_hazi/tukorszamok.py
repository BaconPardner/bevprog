def main():
  tukorszam = input("Tükörszámok\nAdjon meg egy számot: ")

  if tukorszam == ''.join(reversed(tukorszam)):
    print("Tükörszám")
  else:
    print("Nem tükörszám")

if __name__ == "__main__":
  main()