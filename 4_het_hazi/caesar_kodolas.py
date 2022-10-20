MAGIC_NUMBER = 3
DEFAULT_TEXT = "kwwsv=22|rxwx1eh2gTz7z<Zj[fT"

def decoder(text: str, number: int):
  return ''.join([ chr(ord(i) - number) for i in text ])

  # decoded_text = ""
  # for i in range(len(text)):
  #   char = text[i]
  #   decoded_text += chr(ord(char) - MAGIC_NUMBER)
  
  # return decoded_text

def main():
  text = input("Adjon meg egy titkosított szöveget melyet dekódolni akar: ")

  print(f"Dekódolt szöveg: {decoder(text, MAGIC_NUMBER)}")

if __name__ == "__main__":
  main()
