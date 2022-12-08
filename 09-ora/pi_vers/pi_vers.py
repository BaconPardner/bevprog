def main():
    with open('pi_vers.txt', 'r') as f1, open('text.txt', 'w') as f2:
        li = [len(i) for i in f1.read().split(' ')]

        print(li[0], file=f2)

if __name__ == "__main__":
    main()
