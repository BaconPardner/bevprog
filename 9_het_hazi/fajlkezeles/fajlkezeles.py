def main():
    with open('string1.py', 'r') as string1, open('string2.py', 'w') as string2:
        lines = string1.readlines()

        [print(l, file=string2)
         for l in lines if not l.startswith("#") if l.rstrip()]


if __name__ == "__main__":
    main()
