MAGIC_NUMBER = 2
TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def decoder(text: str, number: int):
    return ''.join([chr(ord(i) + number) for i in text])


def main():
    print(f"Dekódolt szöveg: {decoder(TEXT, MAGIC_NUMBER)}")

    print(chr(67))


if __name__ == "__main__":
    main()
