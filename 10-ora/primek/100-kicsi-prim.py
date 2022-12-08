import prime as p


def main():
    for i in range(1, 100):
        if p.is_prime(i):
            print(i)


if __name__ == "__main__":
    main()
