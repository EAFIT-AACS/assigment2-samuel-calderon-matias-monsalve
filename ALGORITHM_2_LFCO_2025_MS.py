import time

class PDA:
    def __init__(self):
        self.stack = []
        self.state = "q0"

    def process_string(self, input_string):
        self.stack = ["$"]
        self.state = "q0"
        for char in input_string:
            if char == "a":
                self.stack.append("A")
            elif char == "b":
                if self.stack and self.stack[-1] == "A":
                    self.stack.pop()
                else:
                    return False
        return self.stack == ["$"]

if __name__ == "__main__":
    print("\n=== Processing Strings with PDA ===\n")
    time.sleep(1.5)

    # Leer las cadenas desde strings.txt
    with open("strings.txt", "r") as file:
        strings = [line.strip() for line in file if line.strip()]

    pda = PDA()
    for string in strings:
        time.sleep(1)
        result = pda.process_string(string)
        print(f"The string '{string}' is {'ACCEPTED' if result else 'REJECTED'} by the PDA.")
    time.sleep(1)
    print("\nProcessing completed!\n")
    time.sleep(1)
