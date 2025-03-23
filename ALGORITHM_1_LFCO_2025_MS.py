import random, time


def generate_valid_strings(n):
    valid_strings = set()
    while len(valid_strings) < n:
        num_a = random.randint(1, 8)
        valid_strings.add('a' * num_a + 'b' * num_a)
    return list(valid_strings)

def generate_invalid_strings(n):
    invalid_strings = set()
    while len(invalid_strings) < n:
        num_a = random.randint(1, 5)
        num_b = random.randint(1, 5)
        if num_a != num_b:
            invalid_strings.add('a' * num_a + 'b' * num_b)
    return list(invalid_strings)

if __name__ == "__main__":
    print("\n=== Generating Strings ===\n")
    time.sleep(1.5)

    valid = generate_valid_strings(2)
    invalid = generate_invalid_strings(2)

    print("Generated Strings:")
    for string in valid + invalid:
        time.sleep(1)
        print(f"  - {string}")
    time.sleep(1)
    print("\nSaving strings to 'strings.txt'...")
    time.sleep(1.5)
    with open("strings.txt", "w") as file:
        for string in valid + invalid:
            file.write(f"{string}\n")
    time.sleep(1)
    print("Strings saved successfully!\n")
    time.sleep(1)
