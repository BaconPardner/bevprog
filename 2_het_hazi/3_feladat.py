def main():
    sodium = int(input("Sodium: "))
    chlorine = int(input("Chlorine: "))
    sodium_chloride = 0
    excessSodium = 0
    excessChlorine = 0

    # if sodium == chlorine * 2: 
    #     sodium_chloride = chlorine * 2
    # elif sodium > chlorine * 2:
    #     sodium_chloride = chlorine * 2
    #     excessChlorine = (sodium - chlorine * 2) * 2
    # else:
    #     sodium_chloride = sodium
    #     excessSodium = chlorine * 2 - sodium

    for i in range(2, sodium + 1):
      sodium = sodium - 2
      chlorine = chlorine - 1
      sodium_chloride = sodium_chloride + 2
      
    excessSodium = sodium
    excessChlorine = chlorine

    print(f"Létrejött só (nátrium-klorid): {sodium_chloride},\nmaradék nátriumatom: {excessSodium},\nmaradék klóratom: {excessChlorine}")

if __name__ == "__main__":
    main()