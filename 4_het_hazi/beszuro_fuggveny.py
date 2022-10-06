def inserter(sentence, param):

  words = sentence.split(' ')

  last_word_index = len(words) - 1
  last_word = words[last_word_index]

  words_without_last_item = ' '.join(words[: last_word_index]) 

  return f"{words_without_last_item} {param} {last_word}"

def main():

  sentence = input("Adjon meg egy szót: ")
  param = input("Adjon meg egy másik szót melyet az előző elé szúrunk: ")

  print(inserter(sentence, param))

if __name__ == "__main__":
  main()