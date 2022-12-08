import math

def distance(p1, p2):
    q1 = (p2[1] - p1[1])
    q2 = (p2[0] - p1[0])

    return math.sqrt(q1 ** 2 + q2 ** 2)

def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()
