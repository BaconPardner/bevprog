MAGIC_NUMBER = 3
DEFAULT_TEXT = "kwwsv=22|rxwx1eh2gTz7z<Zj[fT"

def decoder(text):
  decoded_text = ""
  for i in range(len(text)):
    char = text[i]
    decoded_text += chr(ord(char) - MAGIC_NUMBER)
  
  return decoded_text

def main():
  text = input("Adjon meg egy titkosított szöveget melyet dekódolni akar: ")

  print(f"Dekódolt szöveg: {decoder(text)}")

if __name__ == "__main__":
  main()
