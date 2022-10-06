def valid(text, chars):
  vaild_text = ""

  for i in text:
    for j in chars:
      if i == j:
        vaild_text += i

  return vaild_text

def main():
  text = input("Adjon meg egy karakterláncot: ")

  output = valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

  print(f"-> {output}")

if __name__ == "__main__":
  main()