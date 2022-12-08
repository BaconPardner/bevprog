import requests


def main():

    query = input("pokemon: ")
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{query}")
    data = res.json()

    abilities_number = len(data["abilities"])
    first_move = data["moves"][0]["move"]["name"]

    def stats(n):
        return data["stats"][n]["base_stat"]

    health = stats(0)
    attack = stats(1)
    defense = stats(2)
    speed = stats(3)
    weight = data["weight"]

    print(f"Number of abilities: {abilities_number}")
    print(f"First move: {first_move}")
    print(f"Health: {health}")
    print(f"Attack: {attack}")
    print(f"Defense: {defense}")
    print(f"Speed: {speed}")
    print(f"Weight: {weight}")


if __name__ == "__main__":
    main()
