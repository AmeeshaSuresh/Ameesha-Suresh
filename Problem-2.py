def first_n_odds(n: int):
    return list(range(1, 2*n, 2))

if __name__ == "__main__":
    try:
        n = int(input("Enter a number: ").strip())
        if n <= 0:
            print("")  
        else:
            series = first_n_odds(n)
            print(", ".join(map(str, series)))
    except ValueError:
        print("Invalid input")
