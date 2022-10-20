def fibonacci(sorszam: int):
  i, n_1, n_2 = 0, 0, 1

  while i < sorszam:
    # print(n_1)
    k = n_1 + n_2

    n_1, n_2 = n_2, k

    i += 1

  return n_1

def main():
  sorszam  = int(input("Fibonacci sorozat\nAdja meg az n. tag sorszámát: "))
  print(f"A Fibonacci sorozat {sorszam}. tagja: {fibonacci(sorszam)}")

if __name__ == "__main__":
  main()