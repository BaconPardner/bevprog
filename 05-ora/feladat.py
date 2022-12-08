rang_dict = {
  (0, 0) : "Intern",
  (1, 2) : "Junior",
  (3, 5) : "Medior"
}

class Fejleszto:
  def __init__(self, nev: str, fizetes: int, ev: int = 0, rang: str = "Junior"):
    self.nev = nev
    self.fizetes = fizetes
    self.ev = ev
    self.rang = rang

  def fizetes_emeles(self, fizetes = 10000):
    self.fizetes += fizetes

  def ev_noveles(self):
    self.ev += 1
  
  def fejleszto_rang(self):
    self.rang = [ value for [min_ev, max_ev], value in rang_dict.items() if self.ev >= min_ev and self.ev <= max_ev ][0] or "Senior"

    # for [min_ev, max_ev], value in rang_dict.items():
    #   if self.ev >= min_ev and self.ev <= max_ev:
    #     self.rang = value
    #     break
    #   elif (self.ev > 5):
    #     self.rang = "Senior"

  def __str__(self) -> str:
    return f"Név: {self.nev}\t Rang: {self.rang}\tFizetés: {self.fizetes}\tEltöltött évek: {self.ev}"

def main():
  f1 = Fejleszto("asd", 123)

  print(f1)

  # test
  f1.ev_noveles()
  f1.ev_noveles()
  f1.ev_noveles()
  f1.fejleszto_rang()
  f1.fizetes_emeles()
  f1.fizetes_emeles(2000)
  print(f1)


if __name__ == "__main__":
  main()