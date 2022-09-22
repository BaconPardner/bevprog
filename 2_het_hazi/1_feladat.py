US_DRINKING_AGE = 21
HU_SMOKING_AGE = 18
DRIVING_AGE = 16
SHREK_2_PG_RATE = 12


# Kérd be egy felhasználó életkorát, és döntsd el hogy:

def main():
  age = int(input("Add meg az életkorod: "))

# Fogyaszthat-e legálisan alkoholt Amerikában? (21 év)
  if age >= US_DRINKING_AGE:
    print("\tFogyaszthat alkoholt legálisan Amerikában.")
  elif age < US_DRINKING_AGE:
    print("\tNem fogyaszthat alkoholt legálisan Amerikában.")

# Vásárolhat-e dohányterméket Magyarországon? (18 év)
  if age >= HU_SMOKING_AGE:
    print("\tVásárolhat dohányterméket Magyarországon.")
  elif age < HU_SMOKING_AGE:
    print("\tNem vásárolhat dohányterméket Magyarországon.")

# Szerezhet-e jogosítványt? (16 év)
  if age >= DRIVING_AGE:
    print("\tSzerezhet jogosítványt.")
  elif age < DRIVING_AGE:
    print("\tNem szerezhet jogosítványt.")

# Megnézheti-e egyedül a Shrek 2-t?
  if age >= SHREK_2_PG_RATE:
    print("\tMegnézheti egyedül a Shrek 2-t.")
  elif age < SHREK_2_PG_RATE:
    print("\tNem nézheti meg egyedül a Shrek 2-t.")


if __name__ == "__main__":
  main()