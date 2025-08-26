def parse_numbers(s: str):
    s = s.strip()
    if not s:
        return [1,2,8,9,12,46,76,82,15,20,30]
    s = s.replace(",", " ")
    parts = [p for p in s.split() if p]
    return [int(p) for p in parts]

if __name__ == "__main__":
    try:
        raw = input("Enter numbers (comma/space separated), or press Enter to use sample: ")
        nums = parse_numbers(raw)
        result = {}
        for k in range(1, 10):
            count = sum(1 for n in nums if n % k == 0)
            result[k] = count
        pairs = [f"{k}: {result[k]}" for k in range(1, 10)]
        print("{", end="")
        print(", ".join(pairs), end="")
        print("}")
    except ValueError:
        print("Invalid input (non-integer found)")
