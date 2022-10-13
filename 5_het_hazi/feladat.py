class Fejleszto:
  def __init__(self, nev, fizetes, ev = 0, rang = "Junior"):
    self.nev = nev
    self.fizetes = fizetes
    self.ev = ev
    self.rang = rang

  def fizetes_emeles(self, fizetes = 10000):
    self.fizetes += fizetes

  def ev_noveles(self):
    self.ev += 1
  
  def fejleszto_rang(self):
    rang_dict = {
      "Intern" : [0, 0],
      "Junior" : [1, 2],
      "Medior" : [3, 5]
    }

    for key, [min_ev, max_ev] in rang_dict.items():
      if self.ev >= min_ev and self.ev <= max_ev:
        self.rang = key
        break
      elif (self.ev > 5):
        self.rang = "Senior"

def main():
  f1 = Fejleszto("asd", 123)

  print(f"Név: {f1.nev}\t Rang: {f1.rang}\tFizetés: {f1.fizetes}\tEltöltött évek: {f1.ev}")

  # test
  f1.ev_noveles()
  f1.ev_noveles()
  f1.ev_noveles()
  f1.fejleszto_rang()
  f1.fizetes_emeles()
  print(f"Név: {f1.nev}\t Rang: {f1.rang}\tFizetés: {f1.fizetes}\tEltöltött évek: {f1.ev}")

if __name__ == "__main__":
  main()