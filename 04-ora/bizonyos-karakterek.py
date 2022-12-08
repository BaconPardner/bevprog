def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
  # vaild_text = ""

  # for i in text:
  #   for j in chars:
  #     if i == j:
  #       vaild_text += i

  # return vaild_text

  return "".join([i for i in text for j in chars if i == j])

def main():
  o1 = valid("Barking!")
  o2 = valid("KL754", "0123456789")
  o3 = valid("BEAN", "abcdefghijklmnopqrstuvwxyz")

  print(f"-> {o1, o2, o3}")

if __name__ == "__main__":
  main()