def first_n_odds(n: int):
    return list(range(1, 2*n, 2))

if __name__ == "__main__":
    try:
        a = int(input("Enter a number: ").strip())
        if a <= 0:
            print("")
        else:
            terms = a if a % 2 == 1 else a - 1
            series = first_n_odds(terms)
            print(", ".join(map(str, series)))
    except ValueError:
        print("Invalid input")
