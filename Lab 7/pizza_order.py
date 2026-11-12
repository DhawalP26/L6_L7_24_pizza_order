
TOPPINGS = {
    "cheese": 40,
    "olives": 30,
    "onion": 20,
    "paneer": 50
}

SIZES = {
    "S": 8,
    "M": 10,
    "L": 12
}


def toppings_price(toppings_csv):
    # Validate input type
    if not isinstance(toppings_csv, str):
        raise ValueError("Toppings must be provided as a string")

    total = 0

    # Reject empty input
    if not toppings_csv.strip():
        raise ValueError("At least one topping must be provided")

    for t in toppings_csv.split(','):
        topping = t.strip().lower()

        # Reject empty or unknown toppings
        if not topping or topping not in TOPPINGS:
            raise ValueError(f"Invalid topping: {t}")

        total += TOPPINGS[topping]

    return total


def pizza_inches(size):
    # Validate input type
    if not isinstance(size, str):
        raise ValueError("Pizza size must be a string")

    size = size.strip().upper()

    # Validate pizza size
    if size not in SIZES:
        raise ValueError("Invalid pizza size. Choose S, M or L")

    return SIZES[size]


def split_bill(text):
    # Validate input type
    if not isinstance(text, str):
        raise ValueError("Bill details must be a string")

    # Ensure exactly one separator exists
    if text.count('/') != 1:
        raise ValueError("Format must be total/people")

    total, people = text.split('/')

    try:
        total = int(total.strip())
        people = int(people.strip())
    except ValueError:
        raise ValueError("Total and people must be integers") from None

    # Validate total and number of people
    if total < 0:
        raise ValueError("Total cannot be negative")

    if people <= 0:
        raise ValueError("Number of people must be positive")

    return round(total / people, 2)


def main():
    print("==== Running toppings_price ====")
    user_input = input("Enter toppings as CSV (e.g. cheese,olives): ")

    try:
        result = toppings_price(user_input)
        print("Toppings Price:", result)
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running pizza_inches ====")
    user_input = input("Enter pizza size (S/M/L): ")

    try:
        result = pizza_inches(user_input)
        print("Size in Inches:", result)
    except ValueError as e:
        print("Error:", e)

    print("\n==== Running split_bill ====")
    user_input = input("Enter total and people (e.g. 900/3): ")

    try:
        result = split_bill(user_input)
        print("Per Person:", result)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
