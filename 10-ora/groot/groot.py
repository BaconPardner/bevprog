import sqlite3


def main():
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    res = cur.execute("SELECT name FROM foo")
    print(res.fetchone()[0])


if __name__ == "__main__":
    main()
