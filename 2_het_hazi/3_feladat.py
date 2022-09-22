def main():
    sodium = int(input("Sodium: "))
    chlorine = int(input("Chlorine: "))
    sodium_chloride = 0
    excessSodium = 0
    excessChlorine = 0

    while 1:
      sodium -= 2
      chlorine -= 1
      sodium_chloride += 2

      if sodium == 0:
        break
      elif sodium == 1: 
        break
      
    excessSodium = sodium
    excessChlorine = chlorine

    print(f"Létrejött só (nátrium-klorid): {sodium_chloride},\nmaradék nátriumatom: {excessSodium},\nmaradék klóratom: {excessChlorine}")

if __name__ == "__main__":
    main()