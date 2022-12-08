class Verem:
    def __init__(self) -> None:
        self.li = []

    def betesz(self, value):
        self.li.append(value)

    def meret(self):
        return len(self.li)

    def ures(self):
        return len(self.li) == 0

    def kivesz(self):
        if self.ures():
            return self.li.pop()
        else:
            return None

    def __str__(self) -> str:
        out = "["
        for i in self.li:
            out += f"{i}, "

        return out


def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret())  # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)         # None (jelezzük pl. így, hogy egy üres veremből akarunk kivenni)


if __name__ == "__main__":
    main()
