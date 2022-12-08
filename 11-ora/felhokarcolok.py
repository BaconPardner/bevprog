def main():
    li = [2, 4, 8, 3, 9, 7, 1]
    sum, i, j = 0, 0, 1

    while (j < len(li)):
        n = li[i] - li[j]

        if 1 > n:
            sum += n * -1
        else:
            sum += n

        i += 1
        j += 1

    print(sum)


if __name__ == "__main__":
    main()
