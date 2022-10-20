US_DRINKING_AGE = 21
HU_SMOKING_AGE = 18
DRIVING_AGE = 16
SHREK_2_PG_RATE = 12

legal_things_dict = {
  US_DRINKING_AGE: "Fogyaszthat-e legálisan alkoholt Amerikában?",
  HU_SMOKING_AGE: "Vásárolhat-e dohányterméket Magyarországon?",
  DRIVING_AGE: "Szerezhet-e jogosítványt?",
  SHREK_2_PG_RATE: "Megnézheti-e egyedül a Shrek 2-t?"
}

def main():
  age = int(input("Add meg az életkorod: "))

  print("--------------------------------------------------------------")
  for k, v in legal_things_dict.items():
    if age >= k:
      print(f"{v} Igen\n")
    elif age < k:
      print(f"{v} Nem\n")

if __name__ == "__main__":
  main()