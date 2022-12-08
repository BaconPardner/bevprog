def main():
    anagrams = {
        "A gentleman": " Elegant man",
        "Debit card": " Bad credit",
        "Eleven plus two": " Twelve plus one",
        "Hot water": " Worth tea",
        "Vacation time": " I am not active",
        "Conversation": " Voices rant on",
        "The eyes": " They see",
        "Schoolmaster": " The classroom",
        "The country side": " No city dust here",
        "The Detectives": " Detect thieves",
        "Mummy": " My mum",
        "Dormitory": " Dirty room",
        "A decimal point": " I’m a dot in place",
        "Clint Eastwood": " Old west action",
        "Astronomers": " No more stars",
    }

    s = input("Input: ")
    anagram = ""

    for (key, value) in anagrams.items():
        if key.lower() == s.lower():
            anagram = value
            break
        elif value.lower() == s.lower():
            anagram = key
            break

    if len(anagram) > 1:
        print(anagram)
    else:
        print("No anagram found")


if __name__ == "__main__":
    main()
