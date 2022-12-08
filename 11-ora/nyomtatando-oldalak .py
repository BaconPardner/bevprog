def main():
    foo = "1-4,7,9,11-15"
    li = []

    for i in foo.split(","):
        if len(i) >= 3:
            numbers = i.split("-")

            start = int(numbers[0])
            end = int(numbers[1]) + 1

            for n in range(start, end):
                li.append(n)
        else:
            li.append(int(i))

    print(li)


if __name__ == "__main__":
    main()
