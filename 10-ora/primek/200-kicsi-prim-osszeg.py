import prime as p


def main():
    sum = 0

    for i in range(1, 200):
        if p.is_prime(i):
            sum += i

    print(f"200-nél kisebb prímek összege: {sum}")  # 4228


if __name__ == "__main__":
    main()
